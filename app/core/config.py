import os
from typing import Any

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
    DB_URL:str
    DB_POOL_SIZE:int
    DB_MAX_OVERFLOW:int
    LLM_MODEL:str

settings = Settings()  # type: ignore