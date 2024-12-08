from sqlmodel import SQLModel, Field


class Score(SQLModel, table=True):
    __tablename__ = "score"
    id: int = Field(default_factory=int, primary_key=True)
    temps: int = Field(nullable=False)
    tentative: int = Field(nullable=False)
    Score: int = Field(nullable=False, default=0)
    user_id: int = Field(foreign_key="users.id", nullable=False)
