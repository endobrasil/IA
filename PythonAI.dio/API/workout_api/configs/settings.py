from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str=Field(default='postgresql+asyncpg://workout:workout@192.168.56.101/workout')

settings = Settings()