# Database Models Package
# Job Application Assistance System

from .base import Base
from .user import User, UserProfile, UserSkill, UserExperience
from .application import Application, ApplicationStatusHistory, GeneratedContent
from .job import Company, JobPosting, JobSearchPreference
from .automation import AutomationTask, BrowserSession
from .analytics import UserAnalytics, PlatformMetrics

__all__ = [
    # Base
    "Base",
    
    # User Management
    "User",
    "UserProfile", 
    "UserSkill",
    "UserExperience",
    
    # Application Management
    "Application",
    "ApplicationStatusHistory",
    "GeneratedContent",
    
    # Job Management
    "Company",
    "JobPosting",
    "JobSearchPreference",
    
    # Automation
    "AutomationTask",
    "BrowserSession",
    
    # Analytics
    "UserAnalytics",
    "PlatformMetrics",
] 