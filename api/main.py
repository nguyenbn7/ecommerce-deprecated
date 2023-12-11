from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from route.router import api_router
from core.exception import application_exception_handlers
from share.setting import get_cors_settings

app = FastAPI(exception_handlers=application_exception_handlers)

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
