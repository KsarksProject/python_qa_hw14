from dataclasses import dataclass


@dataclass
class Products:
    model: str
    quantity: str
    price: str


product = Products(model="Coal Pilot XX Charcoal Grill", quantity="1", price="123400")