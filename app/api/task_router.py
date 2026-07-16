from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session


from app.dependencies.db import get_db
from app.dependencies.services import get_task_servive
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_services import TaskService
from app.repositories.task_repository import TaskRepository
from app.unit_of_work.uow import unit_of_work


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


repository = TaskRepository()
service = TaskService(repository,unit_of_work)


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task:TaskCreate,
    service: TaskService = Depends(
        get_task_servive
    ),
):
    return service.create_task(service,task)

@router.get(
    "",
    response_model=list[TaskResponse]
)
def get_tasks(
    db:Session = Depends(get_db)
)->list[TaskResponse]:
    return service.get_tasks(db)

@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_tasks_id(
    task_id:int,
    db:Session=Depends(get_db)
)->TaskResponse:
    return service.get_task_by_id(task_id,db)
