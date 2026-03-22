from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Api
    VERSION: str = "0.0.0"
    TITLE: str = "StepContract gateway Api"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
