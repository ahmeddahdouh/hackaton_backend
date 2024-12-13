from src.app.repositories.team_repository import TeamRepository


class TeamService:
    def __init__(self):
        pass

    def create_team(db, team):
        return TeamRepository.create_team(db, team)

    @staticmethod
    def get_all_teams(db):
        return TeamRepository.get_all_teams(db)

    @staticmethod
    def delete_team(db, team_id):
        return TeamRepository.delete_team(db, team_id)

    @staticmethod
    def update_team(db, team_id, team):
        return TeamRepository.update_team(db, team_id, team)
