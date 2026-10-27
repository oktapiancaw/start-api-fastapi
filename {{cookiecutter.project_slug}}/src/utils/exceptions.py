from fastapi import Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    """Base application error. Raise subclasses from services."""

    status_code = 500
    message = "Internal server error"

    def __init__(self, message: str | None = None, status_code: int | None = None):
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        super().__init__(self.message)


class NotFoundError(AppError):
    status_code = 404
    message = "Resource not found"


async def app_error_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, AppError)
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": type(exc).__name__, "message": exc.message},
    )
