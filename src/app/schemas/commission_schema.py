from pydantic import BaseModel


class CommissionBase(BaseModel):

    team_id: int
    user_id: int
    amount: float
