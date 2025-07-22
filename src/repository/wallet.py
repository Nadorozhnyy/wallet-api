from uuid import UUID
from sqlalchemy import select, ScalarResult

from src.models import Wallet
from src.services.base import AppCRUD


class WalletCrud(AppCRUD):
    async def get_wallet_by_id(self, wallet_id: UUID) -> ScalarResult:
        query = await self.db.scalars(select(Wallet).where(Wallet.id == wallet_id))
        return query

    async def update_wallet(self, item) -> Wallet:
        self.db.add(item)
        await self.db.commit()
        await self.db.refresh(item)
        return item

