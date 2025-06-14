from fastapi import APIRouter, HTTPException
from services.product_service import ProductService
from database import SESSION_DEPENDENCY
from schemas.product_add_sheme import ProductAddSheme
from schemas.product_update_sheme import ProductUpdateScheme


router = APIRouter()

@router.get("/")
async def get_products(session: SESSION_DEPENDENCY):
    service = ProductService(session)
    products = await service.get_all()

    return {"success": True, "data": products}


@router.get("/{product_id}")
async def get_product(product_id: int, session: SESSION_DEPENDENCY):
    service = ProductService(session)
    product = await service.get_by_id(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return {"success": True, "data": product}


@router.post("/")
async def create_product(data: ProductAddSheme, session: SESSION_DEPENDENCY):
    service = ProductService(session)

    try:
        new_product = await service.create(data.dict())

        return {
            "success": True,
            "message": "Product created successfully",
            "data": {
                "id": new_product.id,
                "name": new_product.name,
                "description": new_product.description,
                "price": new_product.price
            }
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Error creating product",
            "error": str(e)
        }


@router.patch("/{product_id}")
async def update_product(product_id: int, data: ProductUpdateScheme, session: SESSION_DEPENDENCY):
    service = ProductService(session)

    try:
        updated_product = await service.update(
            product_id, 
            data
        )

        if not updated_product:
            raise HTTPException(status_code=404, detail="Product not found")

        return {
            "success": True,
            "message": "Product updated successfully",
            "data": {
                "id": updated_product.id,
                "name": updated_product.name,
                "description": updated_product.description,
                "price": updated_product.price
            }
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Error delete product",
            "error": str(e)
        }

   
@router.delete("/{product_id}")
async def delete_product(product_id: int, session: SESSION_DEPENDENCY):
    service = ProductService(session)

    try:
        deleted_product = await service.delete(product_id)

        if not deleted_product:
            raise HTTPException(status_code=404, detail="Product not found")

        return {
            "success": True,
            "message": f"Product {deleted_product.id} deleted successfully"
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Error delete product",
            "error": str(e)
        }
