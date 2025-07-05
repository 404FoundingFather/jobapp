"""
User Management Router
Handles user registration, authentication, and profile management
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
import bcrypt
import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr

from app.core.database import get_db
from app.core.config import settings
from app.models.user import (
    User, UserProfile, UserSkill, UserExperience,
    UserCreate, UserUpdate, UserResponse,
    UserProfileCreate, UserProfileUpdate, UserProfileResponse,
    UserSkillCreate, UserSkillUpdate, UserSkillResponse,
    UserExperienceCreate, UserExperienceUpdate, UserExperienceResponse
)

router = APIRouter()
security = HTTPBearer()


# JWT Token Management
def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_password_hash(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Get current authenticated user from JWT token"""
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


# Authentication endpoints
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        password_hash=hashed_password,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone=user_data.phone,
        is_active=user_data.is_active,
        email_verified=user_data.email_verified,
        subscription_tier=user_data.subscription_tier
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    
    return db_user


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
async def login_user(login: LoginRequest, db: AsyncSession = Depends(get_db)):
    email = login.email
    password = login.password
    # Find user by email
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User account is inactive"
        )
    
    # Update last login
    user.last_login_at = datetime.utcnow()
    await db.commit()
    await db.refresh(user)
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": UserResponse.model_validate({
            "id": str(user.id),
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "is_active": user.is_active,
            "email_verified": user.email_verified,
            "subscription_tier": user.subscription_tier,
            "last_login_at": user.last_login_at,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        })
    }


# User profile endpoints
@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information"""
    return current_user


@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update current user information"""
    update_data = user_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    await db.commit()
    await db.refresh(current_user)
    
    return current_user


@router.get("/me/profile", response_model=UserProfileResponse)
async def get_user_profile(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user profile"""
    result = await db.execute(
        select(UserProfile).where(UserProfile.user_id == current_user.id)
    )
    profile = result.scalar_one_or_none()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    return profile


@router.post("/me/profile", response_model=UserProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_user_profile(
    profile_data: UserProfileCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create user profile"""
    # Check if profile already exists
    result = await db.execute(
        select(UserProfile).where(UserProfile.user_id == current_user.id)
    )
    existing_profile = result.scalar_one_or_none()
    
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile already exists"
        )
    
    # Create new profile
    db_profile = UserProfile(
        user_id=current_user.id,
        **profile_data.dict(exclude={'user_id'})
    )
    
    db.add(db_profile)
    await db.commit()
    await db.refresh(db_profile)
    
    return db_profile


@router.put("/me/profile", response_model=UserProfileResponse)
async def update_user_profile(
    profile_update: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update user profile"""
    result = await db.execute(
        select(UserProfile).where(UserProfile.user_id == current_user.id)
    )
    profile = result.scalar_one_or_none()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    update_data = profile_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(profile, field, value)
    
    await db.commit()
    await db.refresh(profile)
    
    return profile


# User skills endpoints
@router.get("/me/skills", response_model=List[UserSkillResponse])
async def get_user_skills(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user skills"""
    result = await db.execute(
        select(UserSkill).where(UserSkill.user_id == current_user.id)
    )
    skills = result.scalars().all()
    
    return skills


@router.post("/me/skills", response_model=UserSkillResponse, status_code=status.HTTP_201_CREATED)
async def create_user_skill(
    skill_data: UserSkillCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create user skill"""
    db_skill = UserSkill(
        user_id=current_user.id,
        **skill_data.dict(exclude={'user_id'})
    )
    
    db.add(db_skill)
    await db.commit()
    await db.refresh(db_skill)
    
    return db_skill


@router.put("/me/skills/{skill_id}", response_model=UserSkillResponse)
async def update_user_skill(
    skill_id: str,
    skill_update: UserSkillUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update user skill"""
    result = await db.execute(
        select(UserSkill).where(
            UserSkill.id == skill_id,
            UserSkill.user_id == current_user.id
        )
    )
    skill = result.scalar_one_or_none()
    
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    
    update_data = skill_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(skill, field, value)
    
    await db.commit()
    await db.refresh(skill)
    
    return skill


@router.delete("/me/skills/{skill_id}")
async def delete_user_skill(
    skill_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete user skill"""
    result = await db.execute(
        select(UserSkill).where(
            UserSkill.id == skill_id,
            UserSkill.user_id == current_user.id
        )
    )
    skill = result.scalar_one_or_none()
    
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )
    
    await db.delete(skill)
    await db.commit()
    
    return {"message": "Skill deleted successfully"}


# User experience endpoints
@router.get("/me/experiences", response_model=List[UserExperienceResponse])
async def get_user_experiences(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get current user experiences"""
    result = await db.execute(
        select(UserExperience).where(UserExperience.user_id == current_user.id)
    )
    experiences = result.scalars().all()
    
    return experiences


@router.post("/me/experiences", response_model=UserExperienceResponse, status_code=status.HTTP_201_CREATED)
async def create_user_experience(
    experience_data: UserExperienceCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create user experience"""
    db_experience = UserExperience(
        user_id=current_user.id,
        **experience_data.dict(exclude={'user_id'})
    )
    
    db.add(db_experience)
    await db.commit()
    await db.refresh(db_experience)
    
    return db_experience


@router.put("/me/experiences/{experience_id}", response_model=UserExperienceResponse)
async def update_user_experience(
    experience_id: str,
    experience_update: UserExperienceUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update user experience"""
    result = await db.execute(
        select(UserExperience).where(
            UserExperience.id == experience_id,
            UserExperience.user_id == current_user.id
        )
    )
    experience = result.scalar_one_or_none()
    
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found"
        )
    
    update_data = experience_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(experience, field, value)
    
    await db.commit()
    await db.refresh(experience)
    
    return experience


@router.delete("/me/experiences/{experience_id}")
async def delete_user_experience(
    experience_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Delete user experience"""
    result = await db.execute(
        select(UserExperience).where(
            UserExperience.id == experience_id,
            UserExperience.user_id == current_user.id
        )
    )
    experience = result.scalar_one_or_none()
    
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found"
        )
    
    await db.delete(experience)
    await db.commit()
    
    return {"message": "Experience deleted successfully"} 