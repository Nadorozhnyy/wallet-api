from typing import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.exc import SQLAlchemyError

from src.settings import SETTINGS

DB_URL = (
    "postgresql+asyncpg:"
    f"//{SETTINGS.POSTGRES__USER}:"
    f"{SETTINGS.POSTGRES__PASSWORD.get_secret_value()}"
    f"@{SETTINGS.POSTGRES__HOST}:5432"
    f"/{SETTINGS.POSTGRES__DATABASE_NAME}"
)

engine = create_async_engine(
    DB_URL,
    pool_pre_ping=True,
    echo=SETTINGS.POSTGRES__ECHO,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        async_session = AsyncSessionLocal()
        async with async_session as session:
            yield session
    except SQLAlchemyError:
        await session.rollback()
        raise
    finally:
        await session.close()
