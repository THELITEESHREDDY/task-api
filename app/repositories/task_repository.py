from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.task import Task
from app.schemas.task import TaskCreate

class TaskRepository:

    def create(self,db:Session, task_data: TaskCreate) -> Task:
        
        task = Task(title=task_data.title)

        db.add(task)
        db.flush()
        db.refresh(task)

        return task
    
    def get_all(self,db:Session):
        return db.query(Task).all()
    
    def get_by_id(self,task_id,db:Session):

        statement =  select(Task).where(Task.id==task_id)
        
        result = db.execute(statement)
        task = result.scalar_one_or_none()

        return task
    
    
