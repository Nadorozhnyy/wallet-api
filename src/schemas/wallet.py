from uuid import UUID

from pydantic import BaseModel, PositiveInt

from src.schemas.base import BaseSchema
from src.models.wallet import OperationTypeEnum


class WalletBaseSchema(BaseModel):
    amount: int


class ResponseWalletSchema(BaseSchema):
    id: UUID
    amount: int


class OperationWalletSchema(BaseSchema):
    operation_type: OperationTypeEnum
    amount: PositiveInt
