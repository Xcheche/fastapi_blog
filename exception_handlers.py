# exception_handlers.py
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.templating import Jinja2Templates

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Function to register exception handlers
def register_exception_handlers(app):
    @app.exception_handler(StarletteHTTPException)
    async def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
        """ Handle general HTTP exceptions. """
        message = (
            exception.detail
            if exception.detail
            else "An error occurred. Please check your request and try again."
        )

        if request.url.path.startswith("/api"):
            return JSONResponse(
                status_code=exception.status_code,
                content={"detail": message},
            )
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "status_code": exception.status_code,
                "title": exception.status_code,
                "message": message,
            },
            status_code=exception.status_code,
        )

# Handle request validation errors  
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exception: RequestValidationError):
        """ Handle request validation errors. """
        if request.url.path.startswith("/api"):
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                content={"detail": exception.errors()},
            )
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
                "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
                "message": "Invalid request. Please check your input and try again.",
            },
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
