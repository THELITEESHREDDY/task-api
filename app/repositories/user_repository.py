from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    

    def register(
        self,
        db:Session,
        user,
    ):
        db_user = User(
            email=user.email,
            hashed_password=user.hashed_password,
        )

        db.add(db_user)
        db.flush()
        db.refresh(db_user)

        return db_user
    
    def get_by_email(
        self,
        db:Session,
        email:str,
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )