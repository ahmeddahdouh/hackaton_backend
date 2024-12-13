from fastapi import HTTPException
from numpy.lib._datasource import Repository

from src.app.models.commissions import Commission


class CommissionRepository(Repository):

    def __init__(self):
        pass

    @staticmethod
    def get_all_commissions(db):
        return db.query(Commission).all()

    @staticmethod
    def get_commission_by_id(db, id_commission):
        return db.query(Commission).filter(Commission.id == id_commission).first()

    @staticmethod
    def create_commission(db, commission):
        db_commission = Commission(
            team_id=commission.team_id,
            user_id=commission.user_id,
            amount=commission.amount,
        )
        db.add(db_commission)
        db.commit()
        db.refresh(db_commission)
        return db_commission

    @staticmethod
    def update_commission(db, commission, id_commission):
        db_commission = (
            db.query(Commission).filter(Commission.id == id_commission).first()
        )
        if db_commission:
            db_commission.team_id = commission.team_id
            db_commission.user_id = commission.user_id
            db_commission.ammount = commission.ammount
            db.commit()
            db.refresh(db_commission)
            return db_commission
        else:
            HTTPException(status_code=404, detail="commission not found")

    @staticmethod
    def delete_commission(db, id_commission):
        db_commission = (
            db.query(Commission).filter(Commission.id == id_commission).first()
        )
        if db_commission:
            db.delete(db_commission)
            db.commit()
        else:
            HTTPException(status_code=404, detail="commission not found")

