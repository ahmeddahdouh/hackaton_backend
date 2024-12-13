from fastapi import HTTPException

from src.app.models.team_members import TeamMember


class TeamMemberRepository:
    def __init__(self):
        pass

    def create_team_member(db, team_member):
        db_team_member = TeamMember(
            team_id=team_member.team_id, user_id=team_member.user_id
        )

        db.add(db_team_member)
        db.commit()
        db.refresh(db_team_member)
        return db_team_member

    @staticmethod
    def get_all_teams_member(db):
        return db.query(TeamMember).all()

    @staticmethod
    def update_team_members(db, team_member, team_member_id):
        team_member_db = (
            db.query(TeamMember).filter(TeamMember.team_id == team_member_id).first()
        )
        if team_member_db:
            team_member_db.user_id = team_member.user_id
            team_member_db.team_id = team_member.team_id
            return team_member_db
        else:
            raise HTTPException(status_code=404, detail="Team member not found")

    @staticmethod
    def delete_team_members(db, team_member, team_member_id):
        team_member_db = (
            db.query(TeamMember).filter(TeamMember.team_id == team_member_id).first()
        )
        if team_member_db:
            db.delete(team_member_db)
            db.commit()
        else:
            raise HTTPException(status_code=404, detail="Team member not found")
