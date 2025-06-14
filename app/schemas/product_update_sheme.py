# schemas/product.py
from pydantic import BaseModel, Field
from typing import Optional

class ProductUpdateScheme(BaseModel):
    name: Optional[str] = Field(None, example="New Product Name")
    description: Optional[str] = Field(None, example="Updated description")
    price: Optional[float] = Field(None, example=149.99)