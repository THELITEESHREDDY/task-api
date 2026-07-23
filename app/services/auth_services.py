from sqlalchemy.orm import Session
from fastapi import HTTPException,status

from app.security.hashing import verify_password
from app.schemas.user import UserCreateDB,UserCreate
from app.schemas.auth import LoginRequest
from app.security.hashing import hash_password
from app.unit_of_work.uow import unit_of_work
from app.repositories.user_repository import UserRepository
from app.unit_of_work.uow import unit_of_work
from app.security.jwt import create_access_token
from app.schemas.auth import TokenResponse

class AuthService:
    
    
    def __init__(self, repository:UserRepository, uow:unit_of_work):
        self.repository=repository
        self.uow=uow

    
    
    def register(
        self,
        user:UserCreate
    ):
        user = self.repository.get_by_email(
            self.uow.db,
            user.email,
        )

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="email exists"
            )
        
        hashed = hash_password(
            user.password
        )

        db_user = UserCreateDB(
            email=user.email,
            hashed_password=hashed
        )

        created = self.repository.register(
            self.uow.db,
            db_user
        )

        self.uow.commit()

        return created
    
    def login(
        self,
        credentials:LoginRequest
    ):
        user = self.repository.get_by_email(
            self.uow.db,
            credentials.email,
        )

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )
        
        if not verify_password(
            credentials.password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )
        
        token = create_access_token(
            {
                "sub" : str(user.id)
            }
        )

        return TokenResponse(
            access_token=token,
            token_type="bearer",
        )
