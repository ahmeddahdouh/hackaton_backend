from fastapi import APIRouter

from src.app.models.payment import Payment
from src.app.services.payment_service import PaymentService
from src.config.db.database import db_dependency

payment_router = APIRouter(prefix="/payment", tags=["payment"])

@payment_router.get("/")
async def get_all_payment(db:db_dependency):
    return PaymentService.get_all_payments(db)

@payment_router.post("/")
async def create_payment(db:db_dependency,payment:Payment):
    return PaymentService.create_payment(db,payment)

@payment_router.delete("/{payment_id}")
async def delete_payment(db:db_dependency,payment_id:int):
    return PaymentService.delete_payment(db,payment_id)

@payment_router.put("/{payment_id}")
async def update_payment(db:db_dependency, payment:Payment, payment_id):
    return PaymentService.update_payment(db,payment,payment_id)




