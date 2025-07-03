"""
Application Management Models
Models for job applications, status tracking, and generated content
"""

from datetime import date, datetime
from typing import List, Optional, Dict, Any
from sqlalchemy import Column, String, Boolean, Integer, Text, Date, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .base import Base, TimestampMixin, PydanticBase, BaseResponse, BaseCreate, BaseUpdate


# Enums (matching database types)
class ApplicationStatus(str):
    PENDING = "pending"
    SUBMITTED = "submitted"
    REVIEWING = "reviewing"
    INTERVIEWED = "interviewed"
    REJECTED = "rejected"
    OFFERED = "offered"
    WITHDRAWN = "withdrawn"


class ApplicationMethod(str):
    AUTOMATED = "automated"
    MANUAL = "manual"
    REFERRAL = "referral"


class ContentType(str):
    RESUME = "resume"
    COVER_LETTER = "cover_letter"
    FOLLOW_UP_EMAIL = "follow_up_email"


# SQLAlchemy Models
class Application(Base, TimestampMixin):
    """Job application tracking and management"""
    __tablename__ = "applications"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    job_posting_id = Column(UUID(as_uuid=True), ForeignKey("job_postings.id"), index=True)
    company_name = Column(String(255), nullable=False)
    job_title = Column(String(300), nullable=False)
    job_url = Column(String(1000))
    status = Column(String(50), default="pending", index=True)
    application_method = Column(String(50))
    submitted_at = Column(DateTime(timezone=True), index=True)
    last_status_update = Column(DateTime(timezone=True))
    tailored_resume_url = Column(String(500))
    cover_letter_url = Column(String(500))
    notes = Column(Text)
    follow_up_date = Column(Date)
    interview_dates = Column(ARRAY(DateTime(timezone=True)))
    rejection_reason = Column(String(500))
    offer_salary = Column(Integer)
    offer_details = Column(JSONB)
    
    # Relationships
    user = relationship("User", back_populates="applications")
    job_posting = relationship("JobPosting", back_populates="applications")
    status_history = relationship("ApplicationStatusHistory", back_populates="application", cascade="all, delete-orphan")
    generated_content = relationship("GeneratedContent", back_populates="application", cascade="all, delete-orphan")


class ApplicationStatusHistory(Base, TimestampMixin):
    """Application status change history"""
    __tablename__ = "application_status_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id", ondelete="CASCADE"), nullable=False, index=True)
    status = Column(String(50), nullable=False)
    notes = Column(Text)
    changed_by = Column(String(50))
    
    # Relationships
    application = relationship("Application", back_populates="status_history")


class GeneratedContent(Base, TimestampMixin):
    """AI-generated content for applications"""
    __tablename__ = "generated_content"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id", ondelete="CASCADE"), nullable=False, index=True)
    content_type = Column(String(50), nullable=False, index=True)
    content_text = Column(Text)
    file_url = Column(String(500))
    generation_prompt = Column(Text)
    model_used = Column(String(50))
    generation_metadata = Column(JSONB)
    user_approved = Column(Boolean, default=False)
    user_edited = Column(Boolean, default=False)
    
    # Relationships
    application = relationship("Application", back_populates="generated_content")


# Pydantic Models for API
class ApplicationBase(PydanticBase):
    """Base application model"""
    user_id: str
    job_posting_id: Optional[str] = None
    company_name: str
    job_title: str
    job_url: Optional[str] = None
    status: str = "pending"
    application_method: Optional[str] = None
    submitted_at: Optional[datetime] = None
    last_status_update: Optional[datetime] = None
    tailored_resume_url: Optional[str] = None
    cover_letter_url: Optional[str] = None
    notes: Optional[str] = None
    follow_up_date: Optional[date] = None
    interview_dates: Optional[List[datetime]] = None
    rejection_reason: Optional[str] = None
    offer_salary: Optional[int] = None
    offer_details: Optional[Dict[str, Any]] = None


class ApplicationCreate(ApplicationBase):
    """Application creation model"""
    pass


class ApplicationUpdate(BaseUpdate):
    """Application update model"""
    job_posting_id: Optional[str] = None
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    job_url: Optional[str] = None
    status: Optional[str] = None
    application_method: Optional[str] = None
    submitted_at: Optional[datetime] = None
    last_status_update: Optional[datetime] = None
    tailored_resume_url: Optional[str] = None
    cover_letter_url: Optional[str] = None
    notes: Optional[str] = None
    follow_up_date: Optional[date] = None
    interview_dates: Optional[List[datetime]] = None
    rejection_reason: Optional[str] = None
    offer_salary: Optional[int] = None
    offer_details: Optional[Dict[str, Any]] = None


class ApplicationResponse(ApplicationBase, BaseResponse):
    """Application response model"""
    pass


class ApplicationStatusHistoryBase(PydanticBase):
    """Base application status history model"""
    application_id: str
    status: str
    notes: Optional[str] = None
    changed_by: Optional[str] = None


class ApplicationStatusHistoryCreate(ApplicationStatusHistoryBase):
    """Application status history creation model"""
    pass


class ApplicationStatusHistoryUpdate(BaseUpdate):
    """Application status history update model"""
    status: Optional[str] = None
    notes: Optional[str] = None
    changed_by: Optional[str] = None


class ApplicationStatusHistoryResponse(ApplicationStatusHistoryBase, BaseResponse):
    """Application status history response model"""
    pass


class GeneratedContentBase(PydanticBase):
    """Base generated content model"""
    application_id: str
    content_type: str
    content_text: Optional[str] = None
    file_url: Optional[str] = None
    generation_prompt: Optional[str] = None
    model_used: Optional[str] = None
    generation_metadata: Optional[Dict[str, Any]] = None
    user_approved: bool = False
    user_edited: bool = False


class GeneratedContentCreate(GeneratedContentBase):
    """Generated content creation model"""
    pass


class GeneratedContentUpdate(BaseUpdate):
    """Generated content update model"""
    content_text: Optional[str] = None
    file_url: Optional[str] = None
    generation_prompt: Optional[str] = None
    model_used: Optional[str] = None
    generation_metadata: Optional[Dict[str, Any]] = None
    user_approved: Optional[bool] = None
    user_edited: Optional[bool] = None


class GeneratedContentResponse(GeneratedContentBase, BaseResponse):
    """Generated content response model"""
    pass


# Additional models for application functionality
class ApplicationStatusUpdate(PydanticBase):
    """Application status update request model"""
    status: str
    notes: Optional[str] = None
    changed_by: str = "user"


class ApplicationSummary(PydanticBase):
    """Application summary for dashboard"""
    id: str
    company_name: str
    job_title: str
    status: str
    submitted_at: Optional[datetime] = None
    last_status_update: Optional[datetime] = None
    has_generated_content: bool = False


class ApplicationDashboard(PydanticBase):
    """Application dashboard data"""
    total_applications: int
    applications_by_status: Dict[str, int]
    recent_applications: List[ApplicationSummary]
    upcoming_follow_ups: List[ApplicationSummary] 