from pydantic import BaseModel, Field


class scoreBase(BaseModel):
    temps: int
    tentative: int
    Score: int
    user_id: int
