from fastapi import HTTPException

from src.app.models.generated_kwc import GeneratedKWC


class generatedKwcRepository:
    def __init__(self):
        pass

    @staticmethod
    def create_generated_kwc(db, create_generated_kwc):
        generated_kwc = GeneratedKWC(
        user_id = create_generated_kwc.user_id,
        generated_due = create_generated_kwc.generated_due,
        year = create_generated_kwc.year,
        )
        db.add(generated_kwc)
        db.commit()
        return generated_kwc

    @staticmethod
    def update_generated_kwc(db, generated_kwc, update_kwc_id):
        generated_kwc_db = db.query(GeneratedKWC).filter(GeneratedKWC.id ==update_kwc_id)
        if generated_kwc_db:
            generated_kwc_db.user_id = generated_kwc.user_id
            generated_kwc_db.generated_due = generated_kwc.generated_due
            generated_kwc_db.year = generated_kwc.year
            db.commit()
            return generated_kwc_db
        else :
            raise HTTPException(status_code=404,detail="Generated KWC not found")

    @staticmethod
    def delete_generated_kwc(db, update_kwc_id):
        bdd_generated_kwc = db.query(GeneratedKWC).filter(GeneratedKWC.id ==update_kwc_id).first()
        if bdd_generated_kwc:
            db.delete(bdd_generated_kwc)
            db.commit()
            return {"message":"Deleted Generated KWC"}

        else:
            raise HTTPException(status_code=404,detail="Generated KWC not found")

    @staticmethod
    def get_all_generated_kwc(db):
        return db.query(GeneratedKWC).all()

    @staticmethod
    def get_generated_kwc_by_id(db, generated_kwc_id):
        return db.query(GeneratedKWC).filter(GeneratedKWC.id == generated_kwc_id).first()



