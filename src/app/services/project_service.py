from src.app.repositories.project_repository import ProjectRepository


class ProjectService:
    def __init__(self):
        pass

    def create_project(db, project):
        return ProjectRepository.create_project(db, project)

    @staticmethod
    def get_all_projects(db):
        return ProjectRepository.get_all_projects(db)

    @staticmethod
    def get_project_by_id(db, project_id):
        return ProjectRepository.get_project_by_id(db, project_id)

    @staticmethod
    def update_project(db, project, project_id):
        ProjectRepository.update_project(db, project, project_id)

    @staticmethod
    def delete_project(db, project_id):
        ProjectRepository.delete_project(db, project_id)

    @staticmethod
    def get_project_by_id(db, project_id):
        return ProjectRepository.get_project_by_id(db, project_id)
