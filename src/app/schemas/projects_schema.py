from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import date

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ProjectBase(BaseModel):
    user_id: int
    project_name: str
    project_status: str
    project_type: str
    location: str
    parcelle: Optional[str]
    power_kwc: Optional[float]
    date_completude: Optional[date]
    date_pdb: Optional[date]
    amount_due_client: Optional[float]
    apporteur_affaire: Optional[str]
    client_name: str
    client_number: str
