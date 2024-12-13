from src.app.repositories.team_member_repository import TeamMemberRepository


class TeamMemberService:
    def __init__(self):
        pass

    def create_team_member(db, team_member):
        return TeamMemberRepository.create_team_member(db, team_member)

    @staticmethod
    def get_all_teams_member(db):
        return TeamMemberRepository.get_all_teams_member(db)

    @staticmethod
    def update_team_member(db, team_member, team_member_id):
        return TeamMemberRepository.update_team_members(db, team_member, team_member_id)

    @staticmethod
    def delete_team_member(db, team_member_id):
        return TeamMemberRepository.delete_team_members(db, team_member_id)
