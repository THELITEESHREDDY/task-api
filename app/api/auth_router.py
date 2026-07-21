from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session


from app.dependencies.services import get_auth_service
from app.schemas.user import UserResponse, UserCreate 




router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)




@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user:UserCreate,
    service:AuthService = Depends(get_auth_service)
)->UserResponse:
    return service.register(user)