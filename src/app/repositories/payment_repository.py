from fastapi import HTTPException

from src.app.models import payment
from src.app.models.payment import Payment


class PaymentRepository:
    def __init__(self):
        pass

    @staticmethod
    def create_payement(db,payement):
        db_paiement = Payment(
        commission_id = payement.commission_id,
        project_id =payement.project_id,
        amount_paid = payement.amount_paid,
        payment_date = payment.payment_date,
        status = payment.status
        )

        db.add(db_paiement)
        db.commit()
        db.refresh(db_paiement)
        return db_paiement


    @staticmethod
    def update_payement(db, payement,payment_id):
        db_paiement =db.query(Payment).filter(Payment.id ==payment_id).first()
        if db_paiement :
            db_paiement.commission_id=payement.commission_id,
            db_paiement.project_id=payement.project_id,
            db_paiement.amount_paid=payement.amount_paid,
            db_paiement.payment_date=payment.payment_date,
            db_paiement.status=payment.status
            db.add(db_paiement)
            db.commit()
            db.refresh(db_paiement)
            return db_paiement
        else :
            raise HTTPException(status_code=404, detail='Payment not found')

    @staticmethod
    def delete_payement(db,payment_id):
        db_paiement = db.query(Payment).filter(Payment.commission_id == payment_id).first()
        if db_paiement:
            db.delete(db_paiement)
            db.commit()
            return {"message":"payment deleted successfully"}
        else :
            raise HTTPException(status_code=404, detail='Payment not found')

    @staticmethod
    def get_all_payments(db):
        return db.query(Payment).all()

    @staticmethod
    def get_payment_by_id(db,payment_id):
        return db.query(Payment).filter(Payment.id == payment_id).first()







