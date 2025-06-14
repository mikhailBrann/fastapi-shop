from pydantic import BaseModel

class ProductAddSheme(BaseModel):
    name: str
    description: str
    price: float