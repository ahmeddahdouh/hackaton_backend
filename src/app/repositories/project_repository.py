from src.app.models.projects import Project


class ProjectRepository:
    def __init__(self):
        pass

    def create_project(db, project):
        project_db = Project(
            user_id=project.user_id,
            project_name=project.project_name,
            project_status=project.project_status,
            project_type=project.project_type,
            location=project.location,
            parcelle=project.parcelle,
            power_kwc=project.power_kwc,
            date_completude=project.date_completude,
            date_pdb=project.date_pdb,
            amount_due_client=project.amount_due_client,
            apporteur_affaire=project.apporteur_affaire,
            client_name=project.client_name,
            client_number=project.client_number,
        )
        db.add(project_db)
        db.commit()
        db.refresh(project_db)
        return project_db

    @staticmethod
    def get_all_projects(db):
        return db.query(Project).all()

    @staticmethod
    def get_project_by_id(db, project_id):
        return db.query(Project).filter_by(id=project_id).first()

    @staticmethod
    def update_project(db, project, project_id):
        project_db = db.query(Project).filter_by(id=project_id).first()
        project_db.user_id = (project.user_id,)
        project_db.project_name = (project.project_name,)
        project_db.project_status = (project.project_status,)
        project_db.project_type = (project.project_type,)
        project_db.location = (project.location,)
        project_db.parcelle = (project.parcelle,)
        project_db.power_kwc = (project.power_kwc,)
        project_db.date_completude = (project.date_completude,)
        project_db.date_pdb = (project.date_pdb,)
        project_db.amount_due_client = (project.amount_due_client,)
        project_db.apporteur_affaire = (project.apporteur_affaire,)
        project_db.client_name = (project.client_name,)
        project_db.client_number = project.client_number

        db.add(project_db)
        db.commit()
        db.refresh(project_db)
        return project_db

    @staticmethod
    def delete_project(db, project_id):
        project_db = db.query(Project).filter_by(id=project_id).first()
        db.delete(project_db)
        db.commit()
        return {"message": "project deleted successfully"}
