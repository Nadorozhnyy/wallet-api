from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions.base import BaseAPIException


class DBSessionMixin:
    def __init__(self, db: AsyncSession):
        self.db = db


class AppServices(DBSessionMixin):
    pass


class AppCRUD(DBSessionMixin):
    pass


class ServiceResult:
    def __init__(self, value):
        if isinstance(value, BaseAPIException):
            self.success = False
            self.exception_case = value.exception_case
            self.status_code = value.status_code
            self.value = None
            self.exception = value
        else:
            self.success = True
            self.exception_case = None
            self.status_code = None
            self.value = value
            self.exception = None

    def __str__(self):
        if self.success:
            return "[Success]"
        return f'[Exception] "{self.exception_case}"'

    def __repr__(self):
        if self.success:
            return "<ServiceResult Success>"
        return f"<ServiceResult AppException {self.exception_case}>"

    def __enter__(self):
        if self.success:
            return self.value
        else:
            return self.exception

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


async def handle_result(result: ServiceResult):
    if not result.success:
        raise result.exception
    return result.value

