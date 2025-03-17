from dataclasses import dataclass


@dataclass
class Products:
    model: str
    quantity: str
    price: str


product = Products(model="Гриль угольный Coal Pilot XX", quantity="1", price="123 400")