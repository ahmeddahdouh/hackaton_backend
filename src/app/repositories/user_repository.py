from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.app.models.user import User
from src.app.schemas.user_schema import userResponse
from src.config.sécurite.securite import (
    hash_password,
    verify_password,
    create_access_token,
)


class UserRepository:
    def __init__(self):
        pass

    @classmethod
    def create_user(cls, db, user):
        user_db = User(
            first_name=user.first_name,
            last_name=user.last_name,
            password=hash_password(user.password),
            email=user.email,
            phone_number=user.phone_number,
            role=user.role,
            hire_date=user.hire_date,
            grade=user.grade,
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
    def update_user(cls, db, user, user_id):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.password = hash_password(user.password)
            db_user.email = user.email
            db_user.phone_number = user.phone_number
            db_user.role = user.role
            db_user.hire_date = user.hire_date
            db_user.grade = user.grade
            db.commit()
            db.refresh(db_user)
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def delete_user(db, id):
        db_user = db.query(User).filter(User.id == id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def get_users(cls, db) -> list[userResponse]:
        users = db.query(User).all()
        return users

    @classmethod
    def get_user_by_id(cls, db, user_id):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def get_user_by_name(cls, db, user_name):
        db_user = db.query(User).filter().first()
        if db_user:
            return db_user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def login(form_data, db):
        user_data = db.query(User).filter(User.email == form_data.username).first()
        if user_data:
            if verify_password(form_data.password, user_data.password):
                token = create_access_token(data={"sub": form_data.username})
                return {"access_token": token, "token_type": "Bearer","role": user_data.role,"id":user_data.id}
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            raise HTTPException(status_code=404, detail="User not found")
