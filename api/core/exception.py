from dataclasses import dataclass
from typing import Any
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError


@dataclass(frozen=True)
class ErrorResponse:
    message: str
    error: Any | None = None
    errors: Any | None = None


async def api_exception_handler(request: Request, ex: StarletteHTTPException):
    message = ex.detail
    headers = getattr(ex, "headers", None)

    if not message:
        match ex.status_code:
            case status.HTTP_400_BAD_REQUEST:
                message = "We don't talk anymore"
            case status.HTTP_401_UNAUTHORIZED:
                message = "Wait a minute, Who are you"
            case status.HTTP_403_FORBIDDEN:
                message = "You shall not pass"
            case status.HTTP_404_NOT_FOUND:
                message = "Have you seen my cat any where?"
            case default:
                message = "Please report to our support immediately"

    return JSONResponse(
        status_code=ex.status_code,
        content=jsonable_encoder(ErrorResponse(message), exclude_none=True),
        headers=headers,
    )


async def internal_exception_handler(request: Request, exc: Exception):
    # TODO: 
    print(exc)
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder(
            ErrorResponse("Internal Server Error"), exclude_none=True
        ),
    )


async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            ErrorResponse(
                "One or more field can not be validated", errors=exc.errors()
            ),
            exclude_none=True,
        ),
    )


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            ErrorResponse(
                "One or more field can not be validated!!!!", errors=exc.errors()
            ),
            exclude_none=True,
        ),
    )


application_exception_handlers = {
    Exception: internal_exception_handler,
    RequestValidationError: request_validation_exception_handler,
    ValidationError: validation_exception_handler,
    StarletteHTTPException: api_exception_handler,
}
