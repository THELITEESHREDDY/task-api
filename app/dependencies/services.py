from fastapi import Depends
from sqlalchemy.orm import Session


from app.dependencies.db import get_db
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.services.task_services import TaskService
from app.unit_of_work.uow import unit_of_work
from app.services.auth_services import AuthService

def get_task_servive(
        db:Session=Depends(get_db)
):
    
    repo =TaskRepository()

    uow=unit_of_work(db)

    return TaskService(
        repo,
        uow
    )

def get_auth_service(
        db:Session = Depends(get_db),
):
    repo = UserRepository()
    uow = unit_of_work(db)

    return AuthService(repo,uow)