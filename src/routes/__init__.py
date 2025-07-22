from fastapi import APIRouter

from src.routes import (
    wallet
)

api_router = APIRouter()

api_router.include_router(wallet.router, prefix="/wallets", tags=["wallets"])
