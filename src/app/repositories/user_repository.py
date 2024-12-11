from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.models.user import User
from src.app.schemas.user_schema import userResponse
from src.config.sécurité.securité import (
    hash_password,
    verify_password,
    create_access_token,
)


class UserRepository:
    def __init__(self):
        pass

    from sqlalchemy.exc import SQLAlchemyError

    @classmethod
    def create_user(self, db, user):
        user_db = User(
            user_name=user.user_name,
            first_name=user.first_name,
            last_name=user.last_name,
            password=hash_password(user.password),
        )
        try:
            db.add(user_db)
            db.commit()
            db.refresh(user_db)
            return user_db
        except SQLAlchemyError as e:
            db.rollback()
            error_message = str(e.orig) if e.orig else str(e)
            raise HTTPException(status_code=400, detail=error_message)

    @classmethod
    def update_user(self, db, user):
        db_user = db.query(User).filter(User.user_name == user.user_name).first()
        if db_user:
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.password = hash_password(user.password)
            db.commit()
            db.refresh(db_user)
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def delete_user(self, db, user_name):
        db_user = db.query(User).filter(User.user_name == user_name).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return {"message": " User deleted successfully"}

    @classmethod
    def get_users(self, db) -> list[userResponse]:
        users = db.query(User).all()
        return [
            userResponse(
                user_name=user.user_name,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            for user in users
        ]

    @classmethod
    def get_user_by_id(self, db, id):
        db_user = db.query(User).filter(User.id == id).first()
        if db_user:
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def get_user_by_name(self, db, user_name):
        db_user = db.query(User).filter(User.user_name == user_name).first()
        if db_user:
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def login(form_data, db):
        user_data = db.query(User).filter(User.user_name == form_data.username).first()
        if user_data:
            if verify_password(form_data.password, user_data.password):
                token = create_access_token(data={"sub": form_data.username})
                return {"access_token": token, "token_type": "Bearer"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
