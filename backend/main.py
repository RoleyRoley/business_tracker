# Imports
from fastapi import FastAPI
from app.routes.products import router as products_router

app = FastAPI()

app.include_router(products_router, prefix="/products")

@app.get("/")
def home():
    return {"message": "Welcome to the Product Pricing API!"}