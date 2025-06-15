from fastapi import APIRouter, HTTPException
from authx import AuthX, AuthXConfig
import os
from services.auth_service import AuthService
from schemas.auth_user_sheme import AuthUserScheme

router = APIRouter()

SECRET_API_KEY = os.getenv('SECRET_API_KEY')
SECURITY_CONFIG = AuthXConfig()
SECURITY_CONFIG.JWT_SECRET_KEY = SECRET_API_KEY
SECURITY_CONFIG.JWT_TOKEN_LOCATION = ["headers"]
SECURITY = AuthX(SECURITY_CONFIG)

@router.post("/get_token", summary="получить токен")
async def get_token(creeds: AuthUserScheme):
    service = AuthService(SECURITY)
    token = await service.login(creeds)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"access_token": token}