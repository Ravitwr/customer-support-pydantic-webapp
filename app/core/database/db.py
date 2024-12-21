from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

EntityBase = declarative_base()

engine = create_async_engine(
    url=settings.DB_URL,
    pool_size=int(settings.DB_POOL_SIZE),
    max_overflow=int(settings.DB_MAX_OVERFLOW),
)

session_local = async_sessionmaker(
    autocommit=False, autoflush=True, bind=engine)