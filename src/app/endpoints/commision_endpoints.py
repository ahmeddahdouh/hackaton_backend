from fastapi import APIRouter

from src.app.schemas.commission_schema import CommissionBase
from src.app.services.commission_service import CommissionService
from src.config.db.database import db_dependency

commission_router = APIRouter(prefix="/commission", tags=["commission"])


@commission_router.get("/")
async def get_commission(db: db_dependency):
    return CommissionService.get_all_commissions(db)


@commission_router.post("/")
async def create_commission(db: db_dependency, commission: CommissionBase):
    return CommissionService.create_commission(db, commission)


@commission_router.delete("/{id_commission}")
async def delete_commission(db: db_dependency, id_commission):
    return CommissionService.delete_commission(db, id_commission)


@commission_router.put("/{id_commission}")
async def update_commission(db: db_dependency, commission : CommissionBase, id_commission):
    return CommissionService.update_commission(db, commission, id_commission)
