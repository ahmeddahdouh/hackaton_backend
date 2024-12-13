from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TeamMember(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="team.id", nullable=False)
    user_id: int = Field(foreign_key="user.id", nullable=False)

    # Optional relationships for later use
    team: Optional["Team"] = Relationship(back_populates="members")
    user: Optional["User"] = Relationship(back_populates="team_members")
