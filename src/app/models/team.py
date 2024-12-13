from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from src.app.models.commissions import Commission


class Team(SQLModel, table=True):
    __tablename__ = "team"
    id: int = Field(default=None, primary_key=True, index=True)
    manager_id: int = Field(default=None, foreign_key="user.id", nullable=False)
    team_name: str = Field(default=None, nullable=False)
    level: int = Field(default=None, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    # Relation avec le manager
    manager: Optional["User"] = Relationship(back_populates="teams")
    members: List["TeamMember"] = Relationship(back_populates="team")
    commissions: List["Commission"] = Relationship(back_populates="team_commission")
