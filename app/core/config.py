import os
from datetime import timedelta
from typing import Annotated, Any

from pydantic import (
    AnyUrl,
    BeforeValidator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')

def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path, env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str
    APP_VERSION: str
    DEV_MODE:str
    LOG_LEVEL:str


    # CACHE_TTL_IN_SECONDS:int
    # LLM_TEMPERATURE:int
    # LLM_MODEL_NAME:str
    # GCP_PROJECT_ID:str
    # LLM_PROVIDER:str
    # INDEX_NAME:str
    # GEMINI_API_KEY:str


    # ALLOWED_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)]=[]

    # SQLALCHEMY_DATABASE_URI: str
    # DB_POOL_SIZE: int
    # DB_MAX_OVERFLOW: int

    # ES_API_KEY: str
    # SQLALCHEMY_DATABASE_URI: str
    # DB_POOL_SIZE: int
    # DB_MAX_OVERFLOW: int

    # SECRET_KEY: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    # REFRESH_TOKEN_EXPIRE_MINUTES: int
    # DEFAULT_REFRESH_TOKEN_EXPIRE_DELTA: timedelta
    # DEFAULT_ACCESS_TOKEN_EXPIRE_DELTA: timedelta
    # ACCESS_TOKEN_SECRET_KEY: str
    # REFRESH_TOKEN_SECRET_KEY: str

settings = Settings()  # type: ignore