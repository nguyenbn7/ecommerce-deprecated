from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core.error_handler import api_exception_handler
from core.router import api_router
from core.setting import get_cors_settings
from share.model import APIException

app = FastAPI()

# Global error handler for app (exclude uvicorn ...)
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
