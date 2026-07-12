from sqlalchemy.orm import Session

from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate



repository = TaskRepository()


class TaskService:
    def create_task(self, db: Session, task:TaskCreate):
        return repository.create(db,task)