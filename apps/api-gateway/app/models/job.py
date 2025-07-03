"""
Job Discovery Models
Models for companies, job postings, and search preferences
"""

from datetime import date, datetime
from typing import List, Optional, Dict, Any
from sqlalchemy import Column, String, Boolean, Integer, Text, Date, ForeignKey, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy.orm import relationship
from pydantic import BaseModel, validator

from .base import Base, TimestampMixin, PydanticBase, BaseResponse, BaseCreate, BaseUpdate


# Enums (matching database types)
class CompanySize(str):
    STARTUP = "startup"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    ENTERPRISE = "enterprise"


class ExperienceLevel(str):
    ENTRY = "entry"
    MID = "mid"
    SENIOR = "senior"
    LEAD = "lead"
    EXECUTIVE = "executive"


class EmploymentType(str):
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"


class WorkArrangement(str):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"


# SQLAlchemy Models
class Company(Base, TimestampMixin):
    """Company information and details"""
    __tablename__ = "companies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    name = Column(String(255), nullable=False, index=True)
    domain = Column(String(255), index=True)
    industry = Column(String(100), index=True)
    size_category = Column(String(20))
    headquarters_city = Column(String(100))
    headquarters_country = Column(String(50))
    description = Column(Text)
    logo_url = Column(String(500))
    career_page_url = Column(String(500))
    glassdoor_rating = Column(Numeric(3, 2))
    
    # Relationships
    job_postings = relationship("JobPosting", back_populates="company", cascade="all, delete-orphan")


class JobPosting(Base, TimestampMixin):
    """Job posting information from various platforms"""
    __tablename__ = "job_postings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    external_id = Column(String(255))
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), index=True)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text)
    benefits = Column(Text)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    salary_currency = Column(String(3), default="USD")
    experience_level = Column(String(20), index=True)
    employment_type = Column(String(20), index=True)
    work_arrangement = Column(String(20), index=True)
    location_city = Column(String(100), index=True)
    location_state = Column(String(50), index=True)
    location_country = Column(String(50), index=True)
    source_platform = Column(String(50), nullable=False, index=True)
    source_url = Column(String(1000), nullable=False)
    posted_date = Column(Date, index=True)
    expires_date = Column(Date)
    is_active = Column(Boolean, default=True, index=True)
    required_skills = Column(ARRAY(Text))
    preferred_skills = Column(ARRAY(Text))
    embedding = Column("embedding", String)  # pgvector column - will be handled by migration
    
    # Relationships
    company = relationship("Company", back_populates="job_postings")
    applications = relationship("Application", back_populates="job_posting", cascade="all, delete-orphan")


class JobSearchPreference(Base, TimestampMixin):
    """User job search preferences and filters"""
    __tablename__ = "job_search_preferences"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    search_name = Column(String(100), nullable=False)
    target_titles = Column(ARRAY(Text))
    excluded_titles = Column(ARRAY(Text))
    target_companies = Column(ARRAY(Text))
    excluded_companies = Column(ARRAY(Text))
    min_salary = Column(Integer)
    max_salary = Column(Integer)
    experience_levels = Column(ARRAY(Text))
    work_arrangements = Column(ARRAY(Text))
    employment_types = Column(ARRAY(Text))
    locations = Column(ARRAY(Text))
    keywords = Column(ARRAY(Text))
    excluded_keywords = Column(ARRAY(Text))
    is_active = Column(Boolean, default=True, index=True)
    
    # Relationships
    user = relationship("User", back_populates="search_preferences")


# Pydantic Models for API
class CompanyBase(PydanticBase):
    """Base company model"""
    name: str
    domain: Optional[str] = None
    industry: Optional[str] = None
    size_category: Optional[str] = None
    headquarters_city: Optional[str] = None
    headquarters_country: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[str] = None
    career_page_url: Optional[str] = None
    glassdoor_rating: Optional[float] = None


class CompanyCreate(CompanyBase):
    """Company creation model"""
    pass


class CompanyUpdate(BaseUpdate):
    """Company update model"""
    name: Optional[str] = None
    domain: Optional[str] = None
    industry: Optional[str] = None
    size_category: Optional[str] = None
    headquarters_city: Optional[str] = None
    headquarters_country: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[str] = None
    career_page_url: Optional[str] = None
    glassdoor_rating: Optional[float] = None


class CompanyResponse(CompanyBase, BaseResponse):
    """Company response model"""
    pass


class JobPostingBase(PydanticBase):
    """Base job posting model"""
    external_id: Optional[str] = None
    company_id: Optional[str] = None
    title: str
    description: str
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    salary_currency: str = "USD"
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    work_arrangement: Optional[str] = None
    location_city: Optional[str] = None
    location_state: Optional[str] = None
    location_country: Optional[str] = None
    source_platform: str
    source_url: str
    posted_date: Optional[date] = None
    expires_date: Optional[date] = None
    is_active: bool = True
    required_skills: Optional[List[str]] = None
    preferred_skills: Optional[List[str]] = None


class JobPostingCreate(JobPostingBase):
    """Job posting creation model"""
    pass


class JobPostingUpdate(BaseUpdate):
    """Job posting update model"""
    external_id: Optional[str] = None
    company_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    salary_currency: Optional[str] = None
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    work_arrangement: Optional[str] = None
    location_city: Optional[str] = None
    location_state: Optional[str] = None
    location_country: Optional[str] = None
    source_platform: Optional[str] = None
    source_url: Optional[str] = None
    posted_date: Optional[date] = None
    expires_date: Optional[date] = None
    is_active: Optional[bool] = None
    required_skills: Optional[List[str]] = None
    preferred_skills: Optional[List[str]] = None


class JobPostingResponse(JobPostingBase, BaseResponse):
    """Job posting response model"""
    company: Optional[CompanyResponse] = None


class JobSearchPreferenceBase(PydanticBase):
    """Base job search preference model"""
    search_name: str
    target_titles: Optional[List[str]] = None
    excluded_titles: Optional[List[str]] = None
    target_companies: Optional[List[str]] = None
    excluded_companies: Optional[List[str]] = None
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    experience_levels: Optional[List[str]] = None
    work_arrangements: Optional[List[str]] = None
    employment_types: Optional[List[str]] = None
    locations: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    excluded_keywords: Optional[List[str]] = None
    is_active: bool = True


class JobSearchPreferenceCreate(JobSearchPreferenceBase):
    """Job search preference creation model"""
    user_id: str


class JobSearchPreferenceUpdate(BaseUpdate):
    """Job search preference update model"""
    search_name: Optional[str] = None
    target_titles: Optional[List[str]] = None
    excluded_titles: Optional[List[str]] = None
    target_companies: Optional[List[str]] = None
    excluded_companies: Optional[List[str]] = None
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    experience_levels: Optional[List[str]] = None
    work_arrangements: Optional[List[str]] = None
    employment_types: Optional[List[str]] = None
    locations: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    excluded_keywords: Optional[List[str]] = None
    is_active: Optional[bool] = None


class JobSearchPreferenceResponse(JobSearchPreferenceBase, BaseResponse):
    """Job search preference response model"""
    user_id: str


# Additional models for job search functionality
class JobSearchRequest(PydanticBase):
    """Job search request model"""
    query: Optional[str] = None
    location: Optional[str] = None
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    work_arrangement: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    keywords: Optional[List[str]] = None
    excluded_keywords: Optional[List[str]] = None
    limit: int = 50
    offset: int = 0


class JobSearchResponse(PydanticBase):
    """Job search response model"""
    jobs: List[JobPostingResponse]
    total_count: int
    has_more: bool
    search_metadata: Dict[str, Any] 