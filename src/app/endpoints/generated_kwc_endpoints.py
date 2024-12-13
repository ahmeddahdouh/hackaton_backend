from fastapi import APIRouter

from src.app.schemas.generated_kwc_schema import GeneratedKWCBase
from src.app.services.generated_kwc_service import GenratedKwcService
from src.config.db.database import db_dependency

generated_kwc_outlet = APIRouter(prefix="/generated_kwc", tags=["generated_kwc"])

@generated_kwc_outlet.get("/")
async def get_all_generated_kwc(db:db_dependency):
    return GenratedKwcService.get_all_generated_kwc(db)

@generated_kwc_outlet.post("/")
async def create_generated_kwc(db:db_dependency ,generated_kwc:GeneratedKWCBase ):
    return GenratedKwcService.create_generated_kwc(db,generated_kwc)

@generated_kwc_outlet.delete("/{generated_kwc_id}")
async def delete_generated_kwc(db:db_dependency,generated_kwc_id ):
    return GenratedKwcService.delete_generated_kwc(db,generated_kwc_id)

@generated_kwc_outlet.put("/{generated_kwc_id}")
async def update_generated_kwc(db:db_dependency,generated_kwc:GeneratedKWCBase,generated_kwc_id:int ):
    return GenratedKwcService.update_generated_kwc(db,generated_kwc,generated_kwc_id)