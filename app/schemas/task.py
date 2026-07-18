from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title:str

class TaskResponse(BaseModel):
    id:int
    title:str
    completed:bool
    model_config = ConfigDict(from_attributes=True)

class TaskListResponse(BaseModel):
    items: list[TaskResponse]
    total: int
    limit: int
    offset: int
