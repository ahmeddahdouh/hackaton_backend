from src.app.repositories.payment_repository import PaymentRepository


class PaymentService:

    def __init__(self):
        pass

    @staticmethod
    def create_payment(db,payment):
        return PaymentRepository.create_payement(db,payment)


    @staticmethod
    def update_payment(db,payment,id_payment):
        return PaymentRepository.update_payement(db,payment,id_payment)

    @staticmethod
    def delete_payment(db,id_payment):
        return PaymentRepository.delete_payement(db,id_payment)

    @staticmethod
    def get_all_payments(db):
        return PaymentRepository.get_all_payments(db)

    @staticmethod
    def get_payment_by_id(db,id_payment):
        return PaymentRepository.get_payment_by_id(db,id_payment)