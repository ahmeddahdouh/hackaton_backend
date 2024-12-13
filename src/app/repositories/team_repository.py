from fastapi import HTTPException

from src.app.models.team import Team


class TeamRepository:
    def __init__(self):
        pass

    def create_team(db, team):
        team_db = Team(
            manager_id=team.manager_id,
            team_name=team.team_name,
            level=team.level,
            created_at=team.created_at,
        )
        db.add(team_db)
        db.commit()
        db.refresh(team_db)
        return team_db

    @staticmethod
    def get_all_teams(db):
        return db.query(Team).all()

    @staticmethod
    def delete_team(db, team_id):
        db_team = db.query(Team).filter(Team.id == team_id).first()
        if db_team:
            db.delete(db_team)
            db.commit()
            return {"message": "team deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="team not found")

    @staticmethod
    def update_team(db, team_id, team):
        team_db = db.query(Team).filter(Team.id == team_id).first()
        if team_db:
            team_db.manager_id = (team.manager_id,)
            team_db.team_name = (team.team_name,)
            team_db.level = (team.level,)
            team_db.created_at = team.created_at
            db.add(team_db)
            db.commit()
            db.refresh(team_db)
            return team_db
        else:
            raise HTTPException(status_code=404, detail="team not found")
