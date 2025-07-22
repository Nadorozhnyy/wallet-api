from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from src.database import get_session


AsyncSessionDepend = Annotated[async_sessionmaker, Depends(get_session)]