from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from fastapi import Depends

from config import APP_CONFIG


# Создаем движок SQLAlchemy
ENGINE = create_async_engine(APP_CONFIG['DB_URL'])
# Создаем сессию
NEW_SESSION = sessionmaker(bind=ENGINE, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with NEW_SESSION() as session:
        yield session

# Создаем обертку сессии из fastapi
SESSION_DEPENDENCY = Annotated[AsyncSession, Depends(get_session)]



