from fastapi import FastAPI

from app.models import task
from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)







app = FastAPI()


@app.get("/")
def root():
    return {"message" : "Hello Backend"}

