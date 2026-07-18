from sqlalchemy.orm import Session


from app.schemas.user import UserCreateDB
from app.security.hashing import hash_password
from app.unit_of_work.uow import unit_of_work
from app.repositories.user_repository import UserRepository
from app.unit_of_work.uow import unit_of_work

class AuthService:
    
    
    def __init__(self, repository:UserRepository, uow:unit_of_work):
        self.repository=repository
        self.uow=uow

    
    
    def register(
        self,
        db,
        user:UserCreateDB
    ):
        
        hashed = hash_password(
            user.password
        )

        db_user = UserCreateDB(
            email=user.email,
            hashed_password=hashed
        )

        created = self.repository.create(
            db,
            db_user
        )

        self.uow.commit()

        return created
    
