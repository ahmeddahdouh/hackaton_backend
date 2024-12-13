from src.app.repositories.generated_kwc_repository import generatedKwcRepository


class GenratedKwcService:
    def __init__(self):
        pass

    def create_generated_kwc(db,generated_kwc):
        return generatedKwcRepository.create_generated_kwc(db,generated_kwc)

    def update_generated_kwc(db,generated_kwc,generated_kwc_id):
        return generatedKwcRepository.update_generated_kwc(db,generated_kwc,generated_kwc_id)

    @staticmethod
    def delete_generated_kwc(db,generated_kwc_id):
        return generatedKwcRepository.delete_generated_kwc(db,generated_kwc_id)

    def get_all_generated_kwc(db):
        return generatedKwcRepository.get_all_generated_kwc(db)

    def get_generated_kwc_by_id(db,generated_kwc_id):
        return generatedKwcRepository.get_generated_kwc_by_id(db,generated_kwc_id)


