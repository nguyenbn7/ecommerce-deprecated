from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from core import api_router
from share import NotFoundException

app = FastAPI()

origins = ["http://localhost:5173"]

# TODO: dynamic base on environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="www/images"), name="images")

app.include_router(api_router)


@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, ex: NotFoundException):
    return JSONResponse(status_code=ex.status_code, content={"message": ex.message})
