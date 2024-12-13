from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from src.app.models.payment import Payment


class Commission(SQLModel, table=True):
    __tablename__ = "commissions"

    id: int = Field(
        default=None,
        primary_key=True,
        index=True,
    )
    team_id: int = Field(foreign_key="team.id", nullable=False)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    amount: float = Field(nullable=False)

    # Relationships
    team_commission: Optional["Team"] = Relationship(back_populates="commissions")
    user_commission: Optional["User"] = Relationship(back_populates="commissions")
    payments: List["Payment"] = Relationship(back_populates="commission")
