from datetime import datetime

from pydantic import BaseModel


class GeneratedKWCBase(BaseModel):

    user_id: int
    generated_due: datetime
    year: int
