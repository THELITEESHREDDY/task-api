from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException, status

from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate,TaskUpdate
from app.exceptions.task import TaskNotFoundExceptions
from app.core.logging import logger
from app.unit_of_work.uow import unit_of_work


class TaskService:

    def __init__(self, repo:TaskRepository,uow :unit_of_work):
        self.repository = repo
        self.uow=uow


    

    def create_task(self,user_id,task:TaskCreate):
        try:

            logger.info("creating task")
            task= self.repository.create(self.uow.db,user_id,task)
            self.unit_of_work.commit()
            logger.info("Task created with id=%s", task.id)
            return task
        
        except:

            self.uow.rollback()

            raise



    
    def get_tasks(self,user_id:int,limit:int,offset:int):
        print(user_id)
        return self.repository.get_all(self.uow.db,limit,offset,user_id)
    

    def get_task_by_id(self,task_id:int,user_id:int):
        task = self.repository.get_by_id(task_id,user_id,self.uow.db)

        if task is None:
            raise TaskNotFoundExceptions(
                task_id
            )
        
        return task
    

    def update_task(self,data:TaskUpdate,task_id:int,user_id:int):
    
        task = self.repository.get_by_id(task_id,self.uow.db)

        if task is None:
            raise TaskNotFoundExceptions()

        self.repository.update(
            task,
            data,
        )
        unit_of_work.commit()

        return task
    

    def delete_task(self,task_id:int,user_id:int)->None:
        
        task = self.repository.get_by_id(task_id,user_id,self.uow.db)

        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        self.repository.delete(self.uow.db,task)

        unit_of_work.commit()
