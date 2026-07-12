from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session


from app.dependencies.db import get_db
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_services import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


service = TaskService()


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task:TaskCreate,
    db:Session = Depends(get_db),
):
    return service.create_task(db,task)