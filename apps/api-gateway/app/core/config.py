from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Job Application Automation System"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database Configuration
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/jobapp_dev"
    
    # Redis Configuration
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"
    
    # JWT Configuration
    SECRET_KEY: str = "development-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = "your-openai-api-key-here"
    
    # AWS Configuration
    AWS_S3_BUCKET: str = "jobapp-documents-dev"
    AWS_REGION: str = "us-east-1"
    
    # API Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    
    # Logging Configuration
    LOG_LEVEL: str = "DEBUG"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
