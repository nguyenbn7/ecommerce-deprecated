from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.router import api_router
from core.middleware import *
from share.setting import get_cors_settings

app = FastAPI()

app.add_exception_handler(500, internal_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(APIException, api_exception_handler)

# Static files
app.mount("/images", StaticFiles(directory="www/images"), name="images")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_settings().ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(api_router)
