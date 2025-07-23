from uuid import UUID
from fastapi import APIRouter
from starlette import status

from src.services.base import handle_result
from src.schemas import ResponseWalletSchema, OperationWalletSchema
from src.services.wallet import WalletService
from src.dependencies import AsyncSessionDepend

router = APIRouter()


@router.get(
    "/{wallet_uuid}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseWalletSchema,
)
async def get_class_by_id(
        wallet_uuid: UUID,
        session: AsyncSessionDepend,
):
    """
    Возвращает объект Wallet по его id
    """
    res = await WalletService(session).get_wallet_by_id(wallet_uuid)
    return await handle_result(res)


@router.post(
    "/{wallet_uuid}/operation",
    status_code=status.HTTP_200_OK,
    response_model=ResponseWalletSchema,
)
async def get_class_by_id(
        operation_data: OperationWalletSchema,
        wallet_uuid: UUID,
        session: AsyncSessionDepend,
):
    """
    Производит операцию пополнения (DEPOSIT) или списания (WITHDRAW)\n
    с объектом Wallet по его id и возвращает его
    """
    res = await WalletService(session).operation_with_wallet_by_id(wallet_uuid, operation_data)
    return await handle_result(res)
