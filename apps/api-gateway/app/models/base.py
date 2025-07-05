"""
Base Model Class
Provides common functionality for all database models
"""

from datetime import datetime
from typing import Any, Dict
from uuid import UUID
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel as PydanticBaseModel, field_validator


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models"""
    pass


class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps"""
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class PydanticBase(PydanticBaseModel):
    """Base Pydantic model with common configuration"""
    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda v: v.isoformat() if v else None,
            UUID: lambda v: str(v) if v else None
        }
    }


class BaseResponse(PydanticBase):
    """Base response model with common fields"""
    id: str
    created_at: datetime
    updated_at: datetime

    @field_validator('id', mode='before')
    @classmethod
    def ensure_id_is_str(cls, v):
        return str(v) if v is not None else v


class BaseCreate(PydanticBase):
    """Base create model"""
    pass


class BaseUpdate(PydanticBase):
    """Base update model"""
    pass


def model_to_dict(model: Base) -> Dict[str, Any]:
    """Convert SQLAlchemy model to dictionary"""
    return {
        column.name: getattr(model, column.name)
        for column in model.__table__.columns
    } 