from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(exc.detail)},
    )


async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": 400, "message": str(exc.detail)},
    )


def register_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
