from src.app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        pass

    @classmethod
    def create_user(self, db, user):
        return UserRepository.create_user(db, user)

    @classmethod
    def update_user(self, db, user):
        return UserRepository.update_user(db, user)

    @classmethod
    def delete_user(self, db, user_name):
        return UserRepository.delete_user(db, user_name)

    @classmethod
    def get_user(self, db, id_user):
        return UserRepository.get_user_by_id(db, id_user)

    @classmethod
    def get_users(self, db):
        return UserRepository.get_users(db)

    @classmethod
    def get_user_by_name(self, db, user_name):
        return UserRepository.get_user_by_name(db, user_name)

    @staticmethod
    def login(form_data, db):
        return UserRepository.login(form_data, db)
