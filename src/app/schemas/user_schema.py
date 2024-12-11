from typing import Optional

from pydantic import BaseModel, Field


class userBase(BaseModel):
    user_name: str = Field(..., max_length=50)
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., nullable=False, max_length=50)
    password: str = Field(..., nullable=False)


class userResponse(BaseModel):
    user_name: str = Field(..., max_length=50)
    first_name: str = Field(..., max_length=50)
    last_name: Optional[str] = Field(..., nullable=False, max_length=50)

    class Config:
        orm_mode = True
