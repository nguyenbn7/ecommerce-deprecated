from fastapi import Request, status
from fastapi.responses import JSONResponse

from share.model import APIException


async def api_exception_handler(request: Request, ex: APIException):
    message = ex.message
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
            case status.HTTP_500_INTERNAL_SERVER_ERROR:
                message = "Internal Server Error"
            case default:
                message = "Please report to our support immediately"

    return JSONResponse(
        status_code=ex.status_code, content={"message": message}, headers=headers
    )
