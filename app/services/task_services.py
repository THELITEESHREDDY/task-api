from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException, status

from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate





class TaskService:

    def __init__(self, repo:TaskRepository):
        self.repository = repo


    
    def create_task(self,db:Session,task:TaskCreate):
        task= self.repository.create(db,task)
        db.commit()

        return task
    
    def get_tasks(self, db:Session):
        return self.repository.get_all(db)
    
    def get_task_by_id(self,task_id:int,db:Session):
        task = self.repository.get_by_id(task_id,db)

        if task is None:
            raise HTTPException(
                404,
                "Task not found"
            )
        
        return task