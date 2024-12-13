from sys import prefix

from fastapi import APIRouter

from src.app.schemas.projects_schema import ProjectBase
from src.app.services.project_service import ProjectService
from src.config.db.database import db_dependency

project_router = APIRouter(prefix="/projects", tags=["projects"])


@project_router.post("/")
async def create_project(db: db_dependency, project: ProjectBase):
    return ProjectService.create_project(db, project)


@project_router.get("/")
async def get_all_projects(db: db_dependency):
    return ProjectService.get_all_projects(db)


@project_router.put("/")
async def update_project(db: db_dependency, project: ProjectBase, project_id):
    return ProjectService.update_project(db, project, project_id)


@project_router.delete("/")
async def update_(db: db_dependency, project_id):
    return ProjectService.delete_project(db, project_id)

@project_router.get("/{project_id}")
async def get_project_by_id(db: db_dependency, project_id):
    return ProjectService.get_project_by_id(db,project_id)




