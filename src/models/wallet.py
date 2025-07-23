import enum
import uuid

from sqlalchemy import Integer, text
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class OperationTypeEnum(enum.Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class Wallet(Base):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    amount: Mapped[int] = mapped_column(Integer, default=text("0"))

    def __repr__(self):
        return f"wallet id:{self.id}"

    def __str__(self):
        return self.__repr__()
