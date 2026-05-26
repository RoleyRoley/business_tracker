import math

def calculate_product_stats(quantity, unit_cost, shipping_cost, sell_price):
    
    total_cost = (quantity * unit_cost) + shipping_cost

    breakeven_units = math.ceil(total_cost / sell_price)

    profit_per_unit = sell_price - unit_cost

    projected_revenue = quantity * sell_price

    projected_profit = projected_revenue - total_cost

    return {
        "total_cost": total_cost,
        "breakeven_units": breakeven_units,
        "profit_per_unit": profit_per_unit,
        "projected_revenue": projected_revenue,
        "projected_profit": projected_profit
    }