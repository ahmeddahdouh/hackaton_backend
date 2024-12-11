from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Score(SQLModel, table=True):
    __tablename__ = "score"
    id: int = Field(default=None, primary_key=True, nullable=False)
    temps: int = Field(nullable=False)
    tentative: int = Field(nullable=False)
    Score: int = Field(nullable=False, default=0)
    user_id: int = Field(foreign_key="users.id", nullable=False)

    user: Optional["User"] = Relationship(
        back_populates="Scores",
    )
