from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException, status

from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate
from app.exceptions.task import TaskNotFoundExceptions
from app.core.logging import logger
from app.unit_of_work.uow import unit_of_work


class TaskService:

    def __init__(self, repo:TaskRepository,uow :unit_of_work):
        self.repository = repo
        self.uow=uow


    

    def create_task(self,db:Session,task:TaskCreate):
        try:

            logger.info("creating task")
            task= self.repository.create(db,task)
            self.unit_of_work.commit()
            logger.info("Task created with id=%s", task.id)
            return task
        
        except:

            self.unit_of_work.rollback()

            raise



    
    def get_tasks(self, db:Session):
        return self.repository.get_all(db)
    

    def get_task_by_id(self,task_id:int,db:Session):
        task = self.repository.get_by_id(task_id,db)

        if task is None:
            raise TaskNotFoundExceptions(
                task_id
            )
        
        return task
    

    def update_task(self,data:TaskCreate,task_id:int,db:Session):

        task = self.repository.get_by_id(task_id,db)

        if task is None:
            raise TaskNotFoundExceptions()

        self.repository.update(
            task,
            data,
        )
        unit_of_work.commit()

        return task
    

    def delete_task(self,task_id:int,db:Session)->None:
        
        task = self.repository.get_by_id(task_id,db)
        self.repository.delete(db,task)

        unit_of_work.commit()
