import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from src.main import app


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client