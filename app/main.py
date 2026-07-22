from fastapi import FastAPI

from app.models import task
from app.db.database import Base, engine
from app.api.task_router import router as task_router
from app.api.auth_router import router as auth_router
from app.core.exception_handlers import register_exception_handler





app = FastAPI()

register_exception_handler(app)
app.include_router(task_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message" : "Hello Backend"}