"""
Automation Models
Models for automation tasks and browser sessions
"""

from datetime import datetime
from typing import Optional, Dict, Any
from sqlalchemy import Column, String, Boolean, Integer, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .base import Base, TimestampMixin, PydanticBase, BaseResponse, BaseCreate, BaseUpdate


# Enums (matching database types)
class TaskStatus(str):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskType(str):
    JOB_DISCOVERY = "job_discovery"
    RESUME_GENERATION = "resume_generation"
    COVER_LETTER_GENERATION = "cover_letter_generation"
    APPLICATION_SUBMISSION = "application_submission"
    COMPANY_RESEARCH = "company_research"
    SKILLS_EXTRACTION = "skills_extraction"


# SQLAlchemy Models
class AutomationTask(Base, TimestampMixin):
    """Automation task tracking and management"""
    __tablename__ = "automation_tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id"), index=True)
    task_type = Column(String(50), nullable=False, index=True)
    status = Column(String(50), default="pending", index=True)
    priority = Column(Integer, default=5)
    scheduled_at = Column(DateTime(timezone=True), index=True)
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    error_message = Column(Text)
    task_config = Column(JSONB)
    result_data = Column(JSONB)
    
    # Relationships
    user = relationship("User", back_populates="automation_tasks")
    application = relationship("Application")


class BrowserSession(Base, TimestampMixin):
    """Browser session management for automation"""
    __tablename__ = "browser_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    platform = Column(String(50), nullable=False, index=True)
    session_data = Column(JSONB)
    cookies = Column(Text)
    user_agent = Column(String(500))
    proxy_config = Column(JSONB)
    is_active = Column(Boolean, default=True, index=True)
    last_used_at = Column(DateTime(timezone=True))
    expires_at = Column(DateTime(timezone=True))
    
    # Relationships
    user = relationship("User", back_populates="browser_sessions")


# Pydantic Models for API
class AutomationTaskBase(PydanticBase):
    """Base automation task model"""
    user_id: str
    application_id: Optional[str] = None
    task_type: str
    status: str = "pending"
    priority: int = 5
    scheduled_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    retry_count: int = 0
    max_retries: int = 3
    error_message: Optional[str] = None
    task_config: Optional[Dict[str, Any]] = None
    result_data: Optional[Dict[str, Any]] = None


class AutomationTaskCreate(AutomationTaskBase):
    """Automation task creation model"""
    pass


class AutomationTaskUpdate(BaseUpdate):
    """Automation task update model"""
    application_id: Optional[str] = None
    task_type: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None
    scheduled_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    error_message: Optional[str] = None
    task_config: Optional[Dict[str, Any]] = None
    result_data: Optional[Dict[str, Any]] = None


class AutomationTaskResponse(AutomationTaskBase, BaseResponse):
    """Automation task response model"""
    pass


class BrowserSessionBase(PydanticBase):
    """Base browser session model"""
    user_id: str
    platform: str
    session_data: Optional[Dict[str, Any]] = None
    cookies: Optional[str] = None
    user_agent: Optional[str] = None
    proxy_config: Optional[Dict[str, Any]] = None
    is_active: bool = True
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class BrowserSessionCreate(BrowserSessionBase):
    """Browser session creation model"""
    pass


class BrowserSessionUpdate(BaseUpdate):
    """Browser session update model"""
    platform: Optional[str] = None
    session_data: Optional[Dict[str, Any]] = None
    cookies: Optional[str] = None
    user_agent: Optional[str] = None
    proxy_config: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class BrowserSessionResponse(BrowserSessionBase, BaseResponse):
    """Browser session response model"""
    pass


# Additional models for automation functionality
class TaskScheduleRequest(PydanticBase):
    """Task scheduling request model"""
    task_type: str
    application_id: Optional[str] = None
    priority: int = 5
    scheduled_at: Optional[datetime] = None
    task_config: Optional[Dict[str, Any]] = None


class TaskStatusUpdate(PydanticBase):
    """Task status update request model"""
    status: str
    error_message: Optional[str] = None
    result_data: Optional[Dict[str, Any]] = None


class TaskSummary(PydanticBase):
    """Task summary for dashboard"""
    id: str
    task_type: str
    status: str
    priority: int
    scheduled_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None


class AutomationDashboard(PydanticBase):
    """Automation dashboard data"""
    total_tasks: int
    tasks_by_status: Dict[str, int]
    tasks_by_type: Dict[str, int]
    recent_tasks: list[TaskSummary]
    failed_tasks: list[TaskSummary] 