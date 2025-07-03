"""
Analytics Models
Models for user analytics and platform metrics
"""

from datetime import date, datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .base import Base, TimestampMixin, PydanticBase, BaseResponse, BaseCreate, BaseUpdate


# SQLAlchemy Models
class UserAnalytics(Base, TimestampMixin):
    """User analytics and performance metrics"""
    __tablename__ = "user_analytics"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    metric_date = Column(Date, nullable=False, index=True)
    applications_submitted = Column(Integer, default=0)
    jobs_discovered = Column(Integer, default=0)
    resumes_generated = Column(Integer, default=0)
    cover_letters_generated = Column(Integer, default=0)
    interviews_scheduled = Column(Integer, default=0)
    offers_received = Column(Integer, default=0)
    response_rate = Column(Numeric(5, 4))
    time_saved_minutes = Column(Integer, default=0)
    
    # Relationships
    user = relationship("User", back_populates="analytics")


class PlatformMetrics(Base, TimestampMixin):
    """Platform performance and scraping metrics"""
    __tablename__ = "platform_metrics"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    platform_name = Column(String(50), nullable=False, index=True)
    metric_date = Column(Date, nullable=False, index=True)
    total_jobs_scraped = Column(Integer, default=0)
    successful_scrapes = Column(Integer, default=0)
    failed_scrapes = Column(Integer, default=0)
    rate_limit_hits = Column(Integer, default=0)
    detection_events = Column(Integer, default=0)
    average_response_time_ms = Column(Integer)


# Pydantic Models for API
class UserAnalyticsBase(PydanticBase):
    """Base user analytics model"""
    user_id: str
    metric_date: date
    applications_submitted: int = 0
    jobs_discovered: int = 0
    resumes_generated: int = 0
    cover_letters_generated: int = 0
    interviews_scheduled: int = 0
    offers_received: int = 0
    response_rate: Optional[float] = None
    time_saved_minutes: int = 0


class UserAnalyticsCreate(UserAnalyticsBase):
    """User analytics creation model"""
    pass


class UserAnalyticsUpdate(BaseUpdate):
    """User analytics update model"""
    applications_submitted: Optional[int] = None
    jobs_discovered: Optional[int] = None
    resumes_generated: Optional[int] = None
    cover_letters_generated: Optional[int] = None
    interviews_scheduled: Optional[int] = None
    offers_received: Optional[int] = None
    response_rate: Optional[float] = None
    time_saved_minutes: Optional[int] = None


class UserAnalyticsResponse(UserAnalyticsBase, BaseResponse):
    """User analytics response model"""
    pass


class PlatformMetricsBase(PydanticBase):
    """Base platform metrics model"""
    platform_name: str
    metric_date: date
    total_jobs_scraped: int = 0
    successful_scrapes: int = 0
    failed_scrapes: int = 0
    rate_limit_hits: int = 0
    detection_events: int = 0
    average_response_time_ms: Optional[int] = None


class PlatformMetricsCreate(PlatformMetricsBase):
    """Platform metrics creation model"""
    pass


class PlatformMetricsUpdate(BaseUpdate):
    """Platform metrics update model"""
    total_jobs_scraped: Optional[int] = None
    successful_scrapes: Optional[int] = None
    failed_scrapes: Optional[int] = None
    rate_limit_hits: Optional[int] = None
    detection_events: Optional[int] = None
    average_response_time_ms: Optional[int] = None


class PlatformMetricsResponse(PlatformMetricsBase, BaseResponse):
    """Platform metrics response model"""
    pass


# Additional models for analytics functionality
class UserPerformanceSummary(PydanticBase):
    """User performance summary for dashboard"""
    total_applications: int
    total_interviews: int
    total_offers: int
    response_rate: float
    average_time_saved_per_day: int
    success_rate: float


class PlatformPerformanceSummary(PydanticBase):
    """Platform performance summary"""
    platform_name: str
    success_rate: float
    average_response_time_ms: int
    total_jobs_today: int
    rate_limit_status: str


class AnalyticsDashboard(PydanticBase):
    """Analytics dashboard data"""
    user_performance: UserPerformanceSummary
    platform_performance: list[PlatformPerformanceSummary]
    recent_metrics: list[UserAnalyticsResponse]
    trends: dict[str, list[float]] 