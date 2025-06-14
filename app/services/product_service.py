from sqlalchemy import select

from models.product_model import ProductModel
from schemas.product_add_sheme import ProductAddSheme
from schemas.product_update_sheme import ProductUpdateScheme

class ProductService:
    def __init__(self, session):
        self.session = session


    async def get_all(self):
        query = select(ProductModel)
        request = await self.session.execute(query)

        return request.scalars().all()


    async def get_by_id(self, product_id: int):
        query = select(ProductModel).where(ProductModel.id == product_id)
        request = await self.session.execute(query)

        return request.scalar()


    async def create(self, data: ProductAddSheme):
        new_product = ProductModel(**data)

        self.session.add(new_product)
        await self.session.commit()
        await self.session.refresh(new_product)

        return new_product


    async def update(self, product_id: int, data: ProductUpdateScheme):
        product = await self.get_by_id(product_id)

        if not product:
            return None
        
        for key, value in data:
            if value is None:
                continue

            setattr(product, key, value)

        await self.session.commit()
        await self.session.refresh(product)

        return product

   
    async def delete(self, product_id: int):
        product = await self.get_by_id(product_id)

        if not product:
            return None
        
        await self.session.delete(product)
        await self.session.commit()

        return product