# Imports
from fastapi import APIRouter
from pydantic import BaseModel

from schemas.product import ProductCreate

from app.services.pricing import calculate_product_stats

router = APIRouter()


@router.post("/calculate")
def calculate_product(data: ProductCreate):

    stats = calculate_product_stats(
        quantity=data.quantity,
        unit_cost=data.unit_cost,
        shipping_cost=data.shipping_cost,
        sell_price=data.sell_price
    )

    return {
        "name": data.name,
        "quantity": data.quantity,
        "unit_cost": data.unit_cost,
        "shipping_cost": data.shipping_cost,
        "sell_price": data.sell_price,
        "stats": stats
    }