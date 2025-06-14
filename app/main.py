import uvicorn
from fastapi import FastAPI


from config import APP_CONFIG
from database import ENGINE
from models.base import Base

from routes.products import router as products_router


app = FastAPI()

app.include_router(
    products_router, 
    prefix="/products"
)

@app.post("/setup_db")
async def setup_db():
    async with ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        return {
            "success": True,
            "message": "Database setup completed"
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=APP_CONFIG["APP_PORT"])