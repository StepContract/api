from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Api
    VERSION: str = "0.0.0"
    TITLE: str = "StepContract gateway Api"

    # Database
    MARIADB_USER: str
    MARIADB_PASSWORD: str
    MARIADB_DATABASE: str
    DB_PORT: str
    DB_HOST: str
    ECHO: bool = False

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.MARIADB_USER}:{self.MARIADB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.MARIADB_DATABASE}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
