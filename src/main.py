import uvicorn
from fastapi import FastAPI

from src.configs import config, project_meta
from src.routes.v1 import health
from src.utils.exceptions import AppError, app_error_handler

app = FastAPI(
    title=project_meta.title,
    version=project_meta.version,
    description=project_meta.description,
)

app.add_exception_handler(AppError, app_error_handler)
app.include_router(health.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("src.main:app", host=config.host, port=config.port, reload=True)
