from datetime import datetime
from typing import Optional, List

from sqlalchemy import DECIMAL, UniqueConstraint
from sqlmodel import Field, SQLModel, Column, Relationship
from src.app.models.projects import Project


class Payment(SQLModel, table=True):
    __tablename__ = "payment"

    id: int = Field(default=None, primary_key=True, index=True)
    commission_id: int = Field(nullable=False, foreign_key="commissions.id")
    project_id: int = Field(nullable=False, foreign_key="projects.id")
    amount_paid: float
    payment_date: datetime = Field(default_factory=datetime.now, nullable=False)
    status: str = Field(nullable=False, max_length=50)

    project: Optional["Project"] = Relationship(back_populates="payments")
    commission: Optional["Commission"] = Relationship(back_populates="payments")

