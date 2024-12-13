from datetime import datetime
from pydantic import BaseModel

class PaymentBase(BaseModel):
    commission_id: int
    project_id: int
    amount_paid: float
    payment_date: datetime
    status: str
