from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate

class TaskRepository:

    def create(self,db:Session, task_data: TaskCreate) -> Task:
        
        task = Task(title=task_data.title)

        db.add(task)
        db.commit()
        db.refresh(task)

        return task
    
