from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base

class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float] = mapped_column(default=0.0)