from fastapi import HTTPException, Depends
from authx import AuthX, AuthXConfig, RequestToken
import os

from schemas.auth_user_sheme import AuthUserScheme


ACCESS_LOGIN = os.getenv('ACCESS_API_LOGIN')
ACCESS_PASSWORD = os.getenv('ACCESS_API_PASSWORD')


class AuthService:
    def __init__(self, security):
        self.security = security

    async def login(self, creeds: AuthUserScheme):
        if creeds.login == ACCESS_LOGIN and creeds.password == ACCESS_PASSWORD:
            return self.security.create_access_token(uid=ACCESS_LOGIN)
        
        return None
    

    async def check_token(self, token: RequestToken = Depends()):
        # верифицируем токен
        try: 
            self.security.verify_token(token=token)
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")