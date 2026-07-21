from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session


from app.dependencies.services import get_auth_service
from app.schemas.user import UserResponse, UserCreate 
from app.schemas.auth import TokenResponse,LoginRequest
from app.services.auth_services import AuthService




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

@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def login(
    credentials:LoginRequest,
    service:AuthService =Depends(get_auth_service),
):
    return service.login(credentials)