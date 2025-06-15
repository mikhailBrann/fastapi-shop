import uvicorn
from fastapi import FastAPI, Depends


from config import APP_CONFIG
from database import ENGINE
from models.base import Base

from routes.products import router as products_router
from routes.auth import router as auth_router

from services.auth_service import AuthService
from routes.auth import SECURITY as AUTH_SECURITY


app = FastAPI()

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Авторизация 🔐"]
)

app.include_router(
    products_router,
    dependencies=[
        Depends(AuthService(AUTH_SECURITY).check_token)
    ],
    prefix="/products",
    tags=["Товары 🛍️"]
)

@app.post(
    "/setup_db", 
    tags=["Служебные 🛠️"],
    summary="Пересоздать базу данных"
)
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