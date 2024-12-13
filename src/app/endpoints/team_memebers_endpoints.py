from fastapi import APIRouter

from src.app.schemas.team_members_schema import TeamMemberBase
from src.app.services.team_member_service import TeamMemberService
from src.config.db.database import db_dependency

team_members_router = APIRouter(prefix="/team_members", tags=["team_members"])


@team_members_router.post("/")
async def create_team_member(db: db_dependency, team_member: TeamMemberBase):
    return TeamMemberService.create_team_member(db, team_member)


@team_members_router.get("/")
async def get_all_teams_member(db: db_dependency):
    return TeamMemberService.get_all_teams_member(db)


@team_members_router.put("/{team_member_id}")
async def update_team_member(
    db: db_dependency, team_member: TeamMemberBase, team_member_id: int
):
    return TeamMemberService.update_team_member(db, team_member, team_member_id)


@team_members_router.delete("/{team_member_id}")
async def delete_team_member(db: db_dependency, team_member_id: int):
    return TeamMemberService.delete_team_member(db, team_member_id)
