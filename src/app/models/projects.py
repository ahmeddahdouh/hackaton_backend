from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import date


class Project(SQLModel, table=True):
    __tablename__ = "projects"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    project_name: str = Field(max_length=255, nullable=False)
    project_status: str = Field(max_length=50, nullable=False)
    project_type: str = Field(max_length=100, nullable=False)
    location: str = Field(max_length=255, nullable=False)
    parcelle: Optional[str] = Field(max_length=255, default=None)
    power_kwc: Optional[float] = Field(default=None)
    date_completude: Optional[date] = Field(default=None)
    date_pdb: Optional[date] = Field(default=None)
    amount_due_client: Optional[float] = Field(default=None)
    apporteur_affaire: Optional[str] = Field(max_length=255, default=None)
    client_name: str = Field(max_length=255, nullable=False)
    client_number: str = Field(max_length=15, nullable=False)

    user: Optional["User"] = Relationship(back_populates="projects")
    payments: List["Payment"] = Relationship(back_populates="project")
