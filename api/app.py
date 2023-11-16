from fastapi import FastAPI
from cores.apis import router


app = FastAPI()

app.include_router(router)
