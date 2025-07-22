import asyncio
from uuid import UUID
from typing import Dict
from contextlib import asynccontextmanager

from src.models.wallet import OperationTypeEnum
from src.schemas import OperationWalletSchema
from src.services.base import AppServices, ServiceResult
from src.repository.wallet import WalletCrud
from src.exceptions.wallet import WalletNotFound


class WalletService(AppServices):
    _locks: Dict[UUID, asyncio.Lock] = {}
    _lock_for_locks = asyncio.Lock()

    async def _get_or_create_lock(self, wallet_id: UUID):
        async with self._lock_for_locks:
            if wallet_id not in self._locks:
                self._locks[wallet_id] = asyncio.Lock()
            return self._locks[wallet_id]

    @asynccontextmanager
    async def _wallet_lock(self, wallet_id):
        lock = await self._get_or_create_lock(wallet_id)
        async with lock:
            yield

    async def _get_wallet_or_raise(self, wallet_id: UUID):
        wallet = await WalletCrud(self.db).get_wallet_by_id(wallet_id)
        wallet = wallet.first()

        if wallet is None:
            raise WalletNotFound()

        return wallet

    async def get_wallet_by_id(self, wallet_id: UUID) -> ServiceResult:
        wallet = await self._get_wallet_or_raise(wallet_id)
        return ServiceResult(wallet)

    async def operation_with_wallet_by_id(self, wallet_id: UUID, operation_data: OperationWalletSchema):
        async with self._wallet_lock(wallet_id):
            wallet = await self._get_wallet_or_raise(wallet_id)

            if operation_data.operation_type == OperationTypeEnum.DEPOSIT:
                wallet.amount += operation_data.amount
            elif operation_data.operation_type == OperationTypeEnum.WITHDRAW:
                wallet.amount -= operation_data.amount

            update_wallet = await WalletCrud(self.db).update_wallet(wallet)
            return ServiceResult(update_wallet)
