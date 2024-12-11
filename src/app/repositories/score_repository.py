from fastapi import HTTPException

from sqlalchemy.exc import SQLAlchemyError

from src.app.models.score import Score


class ScoreRepository:
    def __init__(self):
        pass

    @classmethod
    def create_score(self, db, score):
        score_db = Score(
            temps=score.temps,
            tentative=score.tentative,
            Score=score.Score,
            user_id=score.user_id,
        )

        try:
            db.add(score_db)
            db.commit()
            db.refresh(score_db)
            return score_db
        except SQLAlchemyError as e:
            error_message = str(e.orig) if e.orig else str(e)
            raise HTTPException(status_code=400, detail=error_message)

    @classmethod
    def get_scores(self, db):
        return db.query(Score).all()

    @classmethod
    def update_score(self, db, score, id_score):
        db_score = db.query(Score).filter(Score.id == id_score).first()
        if db_score:
            db_score.temps = score.temps
            db_score.tentative = score.tentative
            db_score.Score = score.Score
            db.commit()
            db.refresh(db_score)
            return db_score
        else:
            raise HTTPException(status_code=404, detail="Score not found")

    @classmethod
    def delete_score(self, db, score_id):
        db_score = db.query(Score).filter(id == score_id).first()
        if db_score:
            db.delete(db_score)
            db.commit()
            return {"message": "le score a été supprimer correctement "}
        else:
            raise HTTPException(status_code=404, detail="Score not found")

    @staticmethod
    def get_score(db, id_score):
        db_score = db.query(Score).filter(Score.id == int(id_score)).first()
        if db_score:
            return db_score
        else:
            raise HTTPException(status_code=404, detail="Score not found")

    @staticmethod
    def get_all_score(db):
        return db.query(Score).all()
