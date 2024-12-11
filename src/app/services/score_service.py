from src.app.repositories.score_repository import ScoreRepository


class ScoreService:
    def __init__(self):
        pass

    @staticmethod
    def create_score(db , score ):
        return ScoreRepository.create_score(db,score)

    @staticmethod
    def get_scores(db):
        return ScoreRepository.get_scores(db)

    @staticmethod
    def get_score(db,id_score):
        return ScoreRepository.get_score(db,id_score)

    @staticmethod
    def update_score(db, score, id_score):
        return ScoreRepository.update_score(db, score, id_score)

    @staticmethod
    def delete_score( db,id_score):
        return ScoreRepository.delete_score(db,id_score)

    @staticmethod
    def get_all_score(db):
        return ScoreRepository.get_all_score(db)
