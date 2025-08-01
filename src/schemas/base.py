from typing import TypeVar
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


Model = TypeVar("Model", bound=BaseSchema)
