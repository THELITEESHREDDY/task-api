from fastapi import FastAPI

from app.models import task
from app.db.database import Base, engine
from app.api.task_router import router as task_router

Base.metadata.create_all(bind=engine)







app = FastAPI()

app.include_router(task_router)

@app.get("/")
def root():
    return {"message" : "Hello Backend"}

