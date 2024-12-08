from black.cache import field
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship, SQLModel
from typing import List

from src.app.models import score


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True, nullable=False)
    user_name: str = Field(unique=True, nullable=False, max_length=50)
    first_name: str = Field(unique=True, nullable=False, max_length=50)
    last_name: str = Field(unique=True, nullable=False, max_length=50)
    password: str = Field(nullable=False)
    Scores: List["score"] = Relationship(back_populates="score")
