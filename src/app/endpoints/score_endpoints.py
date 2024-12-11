from fastapi import APIRouter

from src.app.schemas.score_schema import scoreBase
from src.app.services.score_service import ScoreService
from src.config.db.database import db_dependency

score_router = APIRouter(prefix="/scores", tags=["Score Endpoints"])


@score_router.post("/")
async def create_score(db: db_dependency, score: scoreBase):
    return ScoreService.create_score(db, score)


@score_router.get("/{id_score}")
async def get_score(db: db_dependency, id_score):
    return ScoreService.get_score(db, id_score)


@score_router.get("/")
async def get_all_score(db: db_dependency):
    return ScoreService.get_all_score(db)


@score_router.delete("/{id_score}")
async def delete_score(db: db_dependency, id_score):
    return ScoreService.delete_score(db, id_score)


@score_router.put("/{id_score}")
async def update_score(db: db_dependency, id_score, score: scoreBase):
    return ScoreService.update_score(db, score, id_score)
