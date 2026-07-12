from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.task import TaskNotFoundExceptions


def register_exception_handler(app: FastAPI):

    @app.exception_handler(TaskNotFoundExceptions)
    async def task_not_found_handler(
        request: Request,
        exc:TaskNotFoundExceptions
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail" : str(exc),
            },
        )