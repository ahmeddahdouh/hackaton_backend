from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class TeamBase(BaseModel):

    manager_id: int
    team_name: str
    level: int
    created_at: datetime
