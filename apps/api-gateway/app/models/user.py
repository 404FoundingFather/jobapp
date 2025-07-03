"""
User Management Models
Models for user authentication, profiles, skills, and experience
"""

from datetime import date, datetime
from typing import List, Optional
from sqlalchemy import Column, String, Boolean, Integer, Text, Date, Numeric, ForeignKey, UniqueConstraint, DateTime, text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, validator

from .base import Base, TimestampMixin, PydanticBase, BaseResponse, BaseCreate, BaseUpdate


# Enums (matching database types)
class SubscriptionTier(str):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"


class SkillCategory(str):
    TECHNICAL = "technical"
    SOFT = "soft"
    LANGUAGE = "language"
    CERTIFICATION = "certification"


class ProficiencyLevel(str):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class WorkArrangement(str):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"


# SQLAlchemy Models
class User(Base, TimestampMixin):
    """User authentication and basic information"""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    is_active = Column(Boolean, default=True, index=True)
    email_verified = Column(Boolean, default=False)
    subscription_tier = Column(String(20), default="free")
    last_login_at = Column(DateTime(timezone=True))
    
    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    skills = relationship("UserSkill", back_populates="user", cascade="all, delete-orphan")
    experiences = relationship("UserExperience", back_populates="user", cascade="all, delete-orphan")
    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")
    search_preferences = relationship("JobSearchPreference", back_populates="user", cascade="all, delete-orphan")
    automation_tasks = relationship("AutomationTask", back_populates="user", cascade="all, delete-orphan")
    browser_sessions = relationship("BrowserSession", back_populates="user", cascade="all, delete-orphan")
    analytics = relationship("UserAnalytics", back_populates="user", cascade="all, delete-orphan")


class UserProfile(Base, TimestampMixin):
    """Extended user profile information"""
    __tablename__ = "user_profiles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    resume_file_url = Column(String(500))
    resume_text = Column(Text)
    linkedin_url = Column(String(255))
    github_url = Column(String(255))
    portfolio_url = Column(String(255))
    phone = Column(String(20))
    location_city = Column(String(100))
    location_state = Column(String(50))
    location_country = Column(String(50))
    willing_to_relocate = Column(Boolean, default=False)
    years_experience = Column(Integer)
    current_title = Column(String(200))
    target_salary_min = Column(Integer)
    target_salary_max = Column(Integer)
    preferred_work_type = Column(String(20))
    
    # Constraints
    __table_args__ = (UniqueConstraint("user_id", name="unique_user_profile"),)
    
    # Relationships
    user = relationship("User", back_populates="profile")


class UserSkill(Base, TimestampMixin):
    """User skills and competencies"""
    __tablename__ = "user_skills"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_name = Column(String(100), nullable=False, index=True)
    skill_category = Column(String(50), index=True)
    proficiency_level = Column(String(20))
    years_experience = Column(Numeric(3, 1))
    is_primary = Column(Boolean, default=False)
    
    # Relationships
    user = relationship("User", back_populates="skills")


class UserExperience(Base, TimestampMixin):
    """User work experience and history"""
    __tablename__ = "user_experiences"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    company_name = Column(String(200), nullable=False)
    job_title = Column(String(200), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    is_current = Column(Boolean, default=False, index=True)
    description = Column(Text)
    achievements = Column(ARRAY(Text))
    technologies_used = Column(ARRAY(Text))
    
    # Relationships
    user = relationship("User", back_populates="experiences")


# Pydantic Models for API
class UserBase(PydanticBase):
    """Base user model"""
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True
    email_verified: bool = False
    subscription_tier: str = "free"


class UserCreate(UserBase):
    """User creation model"""
    password: str
    
    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v


class UserUpdate(BaseUpdate):
    """User update model"""
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    email_verified: Optional[bool] = None
    subscription_tier: Optional[str] = None


class UserResponse(UserBase, BaseResponse):
    """User response model"""
    last_login_at: Optional[datetime] = None


class UserProfileBase(PydanticBase):
    """Base user profile model"""
    resume_file_url: Optional[str] = None
    resume_text: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    phone: Optional[str] = None
    location_city: Optional[str] = None
    location_state: Optional[str] = None
    location_country: Optional[str] = None
    willing_to_relocate: bool = False
    years_experience: Optional[int] = None
    current_title: Optional[str] = None
    target_salary_min: Optional[int] = None
    target_salary_max: Optional[int] = None
    preferred_work_type: Optional[str] = None


class UserProfileCreate(UserProfileBase):
    """User profile creation model"""
    user_id: str


class UserProfileUpdate(BaseUpdate):
    """User profile update model"""
    resume_file_url: Optional[str] = None
    resume_text: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    phone: Optional[str] = None
    location_city: Optional[str] = None
    location_state: Optional[str] = None
    location_country: Optional[str] = None
    willing_to_relocate: Optional[bool] = None
    years_experience: Optional[int] = None
    current_title: Optional[str] = None
    target_salary_min: Optional[int] = None
    target_salary_max: Optional[int] = None
    preferred_work_type: Optional[str] = None


class UserProfileResponse(UserProfileBase, BaseResponse):
    """User profile response model"""
    user_id: str


class UserSkillBase(PydanticBase):
    """Base user skill model"""
    skill_name: str
    skill_category: Optional[str] = None
    proficiency_level: Optional[str] = None
    years_experience: Optional[float] = None
    is_primary: bool = False


class UserSkillCreate(UserSkillBase):
    """User skill creation model"""
    user_id: str


class UserSkillUpdate(BaseUpdate):
    """User skill update model"""
    skill_name: Optional[str] = None
    skill_category: Optional[str] = None
    proficiency_level: Optional[str] = None
    years_experience: Optional[float] = None
    is_primary: Optional[bool] = None


class UserSkillResponse(UserSkillBase, BaseResponse):
    """User skill response model"""
    user_id: str


class UserExperienceBase(PydanticBase):
    """Base user experience model"""
    company_name: str
    job_title: str
    start_date: date
    end_date: Optional[date] = None
    is_current: bool = False
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    technologies_used: Optional[List[str]] = None


class UserExperienceCreate(UserExperienceBase):
    """User experience creation model"""
    user_id: str


class UserExperienceUpdate(BaseUpdate):
    """User experience update model"""
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_current: Optional[bool] = None
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    technologies_used: Optional[List[str]] = None


class UserExperienceResponse(UserExperienceBase, BaseResponse):
    """User experience response model"""
    user_id: str 