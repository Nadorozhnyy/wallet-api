from uuid import UUID

from src.models.wallet import OperationTypeEnum
from src.schemas import OperationWalletSchema
from src.services.base import AppServices, ServiceResult
from src.repository.wallet import WalletCrud
from src.exceptions.wallet import WalletNotFound


class WalletService(AppServices):

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
        wallet = await self._get_wallet_or_raise(wallet_id)

        if operation_data.operation_type == OperationTypeEnum.DEPOSIT:
            wallet.amount += operation_data.amount
        elif operation_data.operation_type == OperationTypeEnum.WITHDRAW:
            wallet.amount -= operation_data.amount

        update_wallet = await WalletCrud(self.db).update_wallet(wallet)
        return ServiceResult(update_wallet)
