from fastapi import FastAPI
from core import api_router

app = FastAPI()

app.include_router(api_router)
