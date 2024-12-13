from src.app.repositories.commission_repository import CommissionRepository


class CommissionService:

    @staticmethod
    def get_all_commissions(db):
        return CommissionRepository.get_all_commissions(db)

    @staticmethod
    def create_commission(db, commission):
        return CommissionRepository.create_commission(db, commission)

    @staticmethod
    def update_commission(db, commission, id_commission):
        return CommissionRepository.update_commission(db, commission, id_commission)

    @staticmethod
    def delete_commission(db, commission_id):
        return CommissionRepository.delete_commission(db, commission_id)

    @staticmethod
    def get_commission_by_id(db, commission_id):
        return CommissionRepository.get_commission_by_id(db, commission_id)
