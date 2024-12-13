from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.app.models.user import UserGrade, UserRole


class userBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., nullable=False, max_length=50)
    password: str = Field(..., nullable=False)
    email: str
    phone_number: int
    role: UserRole
    hire_date: datetime
    grade: UserGrade


class userResponse(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., nullable=False, max_length=50)
    password: str = Field(..., nullable=False)
    manager_id: int
    email: str
    phone_number: int
    role: UserRole
    hire_date: datetime
    grade: UserGrade

    class Config:
        orm_mode = True
