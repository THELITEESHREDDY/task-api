from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.task import Task
from app.schemas.task import TaskCreate,TaskResponse

class TaskRepository:

    def create(
        self,
        db:Session, 
        task_data: TaskCreate
    ) -> Task:
        
        task = Task(title=task_data.title)

        db.add(task)
        db.flush()
        db.refresh(task)

        return task


    def get_all(
        self,
        db: Session,
        completed: bool | None,
        limit: int,
        offset: int,
    ):

        stmt = select(Task)

        if completed is not None:
            stmt = stmt.where(
                Task.completed == completed
            )

        stmt = (
            stmt
            .order_by(Task.id.desc())
            .limit(limit)
            .offset(offset)
        )

        result = db.execute(stmt)

        return result.scalars().all()
    


    def get_by_id(
        self,
        task_id,db:Session
    ):

        statement =  select(Task).where(Task.id==task_id)
        
        result = db.execute(statement)
        task = result.scalar_one_or_none()

        return task
    
    

    def update(
        self, 
        task:TaskCreate,
        data:TaskCreate,
    )->TaskCreate:
        task.title = data.titleSS

        return task
        

    def delete(
        self,
        db:Session,
        task:TaskResponse,
    )->None:
        db.delete(task)