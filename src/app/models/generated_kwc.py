from src.app.models.user import User
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# GENERATED_KWC (id, user_id, generated_due, year)


class GeneratedKWC(SQLModel, table=True):
    __tablename__ = "generated_kwc"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    generated_due: datetime = Field(nullable=False)
    year: int = Field(nullable=False)

    # Relation avec la table User
    user: Optional["User"] = Relationship(back_populates="generated_kwcs")
