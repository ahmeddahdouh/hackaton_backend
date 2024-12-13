from enum import Enum
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from sqlalchemy import Enum as SQLAlchemyEnum, Numeric
from datetime import datetime

from src.app.models.commissions import Commission
from src.app.models.team import Team


class UserRole(str, Enum):
    Administrateur = "ADMIN"
    Utilisateur = "USER"
    CA = "CA"
    Manager = "Manager"


class UserGrade(str, Enum):
    chargeAffaire = "chargeAffaire"
    seniorManager = "seniorManager"
    executiveManager = "executiveManager"
    eliteManager = "eliteManager"
    Manager = "eliteManager"
    SeniorManager = "eliteManager"
    ExecutiveManager = "eliteManager"
    EliteManager = "eliteManager"
    aucun = 'aucun'

# Modèle SQLModel pour la table users
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    first_name: str = Field(max_length=100, nullable=False)
    last_name: str = Field(max_length=100, nullable=False)
    email: str = Field(max_length=150, nullable=False, unique=True)
    password: str = Field(max_length=150, nullable=False)
    phone_number: Optional[str] = Field(max_length=15, nullable=True)
    role: UserRole = Field(sa_column=SQLAlchemyEnum(UserRole))
    hire_date: Optional[datetime] = Field(nullable=True)
    grade: Optional[UserGrade] = Field(sa_column=SQLAlchemyEnum(UserGrade))

    # Relation avec les équipes
    teams: List["Team"] = Relationship(back_populates="manager")
    generated_kwcs: List["GeneratedKWC"] = Relationship(back_populates="user")
    team_members: List["TeamMember"] = Relationship(back_populates="user")
    projects: List["Project"] = Relationship(back_populates="user")
    commissions: List["Commission"] = Relationship(back_populates="user_commission")
