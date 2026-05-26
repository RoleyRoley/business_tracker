# Imports
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.pricing import calculate_product_stats

router = APIRouter()

class ProductCalculationRequest(BaseModel):
    quantity: int
    unit_cost: float
    shipping_cost: float
    sell_price: float

@router.post("/calculate")
def calculate_product(data: ProductCalculationRequest):
    return calculate_product_stats(
        quantity=data.quantity,
        unit_cost=data.unit_cost,
        shipping_cost=data.shipping_cost,
        sell_price=data.sell_price
    )