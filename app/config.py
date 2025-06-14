import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = int(os.getenv('APP_PORT', 8000))
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

APP_CONFIG = {
    'APP_PORT': APP_PORT,
    'DB_URL': f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}",
}