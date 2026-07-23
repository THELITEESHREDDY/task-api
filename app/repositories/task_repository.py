from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.task import Task
from app.schemas.task import TaskCreate,TaskResponse,TaskUpdate

class TaskRepository:

    def create(
        self,
        db:Session,
        user_id:int, 
        task_data: TaskCreate,
    ) -> Task:
        
        task = Task(title=task_data.title,owner_id=user_id)

        db.add(task)
        db.flush()
        db.refresh(task)

        return task


    def get_all(
        self,
        db: Session,
        limit: int,
        offset: int,
        user_id:int
    )->list[TaskResponse]:

        return db.query(Task).filter(Task.owner_id==user_id).all()


    def get_by_id(
        self,
        task_id:int,
        user_id:int,
        db:Session,
    )->Task | None:

       return (
           db.query(Task)
           .filter(
               Task.id == task_id,
               Task.owner_id == user_id,
            )
            .first()
       )
    

    def update(
        self, 
        task:TaskUpdate,
        data:TaskUpdate,
    )->TaskCreate:
        task.title = data.title
        task.completed = data.completed

        return task
        

    def delete(
        self,
        db:Session,
        task:TaskResponse,
    )->None:
        db.delete(task)