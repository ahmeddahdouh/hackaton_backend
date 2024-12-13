from pydantic import BaseModel
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TeamMemberBase(BaseModel):

    team_id: int
    user_id: int
