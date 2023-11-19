from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


# Environment Settings
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
# https://fastapi.tiangolo.com/advanced/settings/?h=setting#pydantic-settings


class CorsSetting(BaseSettings):
    ORIGINS: List[str]
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DatabaseSetting(BaseSettings):
    DB: str
    USER: str
    PASSWORD: str
    HOST: str | None = "localhost"
    PORT: int | None = 5432
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="POSTGRES_"
    )


@lru_cache
def get_database_settings():
    return DatabaseSetting()

@lru_cache
def get_cors_settings():
    return CorsSetting()
