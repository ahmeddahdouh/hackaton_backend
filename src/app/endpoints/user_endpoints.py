from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.app.schemas.user_schema import userBase
from src.app.services.user_service import UserService
from src.config.db.database import db_dependency
from src.config.sécurite.securite import oauth2_scheme

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/")
async def create_users(db: db_dependency, user: userBase):
    return UserService.create_user(db, user)


@user_router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    return UserService.login(form_data, db)


@user_router.get("/")
async def get_users(db: db_dependency):
    return UserService.get_users(db)


@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: db_dependency):
    return UserService.get_user(db, user_id)


@user_router.get("/userName/{user_name}")
async def get_user_by_name(user_name: str, db: db_dependency):
    return UserService.get_user_by_name(db, user_name)


@user_router.put("/{id_user}")
async def update_users(db: db_dependency, user: userBase, id_user: int):
    return UserService.update_user(db, user, id_user)


@user_router.delete("/{id_user}")
async def delete_users(db: db_dependency, id_user: int):
    return UserService.delete_user(db, id_user)
