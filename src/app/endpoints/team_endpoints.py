from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import async_engine_from_config

from src.app.schemas.team_schema import TeamBase
from src.app.schemas.user_schema import userBase
from src.app.services.team_service import TeamService
from src.app.services.user_service import UserService
from src.config.db.database import db_dependency
from src.config.sécurite.securite import oauth2_scheme

team_router = APIRouter(prefix="/teams", tags=["Teams"])


@team_router.post("/")
async def create_team(db: db_dependency, team: TeamBase):
    return TeamService.create_team(db, team)


@team_router.get("/")
async def get_all_teams(db: db_dependency):
    return TeamService.get_all_teams(db)


@team_router.put("/{team_id}")
async def update_team(db: db_dependency, team_id, team: TeamBase):
    return TeamService.update_team(db, team_id, team)


@team_router.delete("/{team_id}")
async def delete_team(db: db_dependency, team_id):
    return TeamService.delete_team(db, team_id)
