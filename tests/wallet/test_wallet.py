import pytest
from uuid import uuid4, UUID
from fastapi import status
from httpx import AsyncClient

from src.services.base import ServiceResult

pytestmark = pytest.mark.asyncio


class TestWalletEndpoints:
    @pytest.fixture
    def wallet_uuid(self):
        return str(uuid4())

    async def test_get_wallet_by_id_success(self, async_client: AsyncClient, wallet_uuid: UUID, mocker):
        wallet_data = {
            "id": str(wallet_uuid),
            "amount": 100
        }
        mock_result = ServiceResult(value=wallet_data)
        mocker.patch(
            "src.services.wallet.WalletService.get_wallet_by_id",
            return_value=mock_result
        )
        response = await async_client.get(f"/api/v1/wallets/{wallet_uuid}")
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data["id"] == str(wallet_uuid)
        assert response_data["amount"] == 100

    async def test_get_wallet_by_id_failed(self, async_client: AsyncClient, wallet_uuid: UUID):
        invalid_uuid = "invalid-uuid"

        response = await async_client.get(f"/api/v1/wallets/{invalid_uuid}")

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_wallet_operation_deposit_success(self, async_client: AsyncClient, wallet_uuid: UUID, mocker):
        operation_data = {
            "operation_type": "DEPOSIT",
            "amount": 100
        }
        wallet_data_after_operation = {
            "id": str(wallet_uuid),
            "amount": 200
        }
        mock_result = ServiceResult(value=wallet_data_after_operation)
        mocker.patch(
            "src.services.wallet.WalletService.operation_with_wallet_by_id",
            return_value=mock_result
        )
        response = await async_client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation",
            json=operation_data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == str(wallet_uuid)
        assert response.json()["amount"] == 200

    async def test_wallet_operation_withdraw_success(self, async_client: AsyncClient, wallet_uuid: UUID, mocker):
        operation_data = {
            "operation_type": "DEPOSIT",
            "amount": 200
        }
        wallet_data_after_operation = {
            "id": str(wallet_uuid),
            "amount": 100
        }
        mock_result = ServiceResult(value=wallet_data_after_operation)
        mocker.patch(
            "src.services.wallet.WalletService.operation_with_wallet_by_id",
            return_value=mock_result
        )
        response = await async_client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation",
            json=operation_data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == str(wallet_uuid)
        assert response.json()["amount"] == 100

    async def test_wallet_operation_amount_failed(self, async_client: AsyncClient, wallet_uuid: UUID):
        operation_data = {
            "operation_type": "DEPOSIT",
            "amount": -50
        }

        response = await async_client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation",
            json=operation_data
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_wallet_operation_amount_zero_failed(self, async_client: AsyncClient, wallet_uuid: UUID):
        operation_data = {
            "operation_type": "DEPOSIT",
            "amount": 0
        }

        response = await async_client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation",
            json=operation_data
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_wallet_operation_operation_type_failed(self, async_client: AsyncClient, wallet_uuid: UUID):
        operation_data = {
            "operation_type": "WRONG_TYPE",
            "amount": 100
        }

        response = await async_client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation",
            json=operation_data
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
