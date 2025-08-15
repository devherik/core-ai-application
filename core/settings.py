import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, ".env")

if os.path.exists(env_path):
    load_dotenv()
else:
    raise FileNotFoundError(f".env file not found at {env_path}")

class Settings(BaseSettings):
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    class Config:
        env_file = env_path
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()