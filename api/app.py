from fastapi import FastAPI
from products import router as products_router
from products_brands import router as products_brands_router
from products_types import router as products_types_router
from account import router as account_router

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}


app.include_router(products_router, prefix="/api")
app.include_router(products_brands_router, prefix="/api")
app.include_router(products_types_router, prefix="/api")
app.include_router(account_router, prefix="/api")
