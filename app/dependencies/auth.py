from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.dependencies.db import get_db
from app.security.jwt import SECRET_KEY,ALGORITHM
from app.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str= Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
    
    repo = UserRepository()
    user = repo.get_by_id(db,int(user_id))

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )
    
    return user