from fastapi import status

from src.exceptions.base import BaseAPIException


class WalletNotFound(BaseAPIException):
    def __init__(self, context: dict = None):
        status_code = status.HTTP_404_NOT_FOUND
        context = {"Error message": "Wallet is not found"}
        BaseAPIException.__init__(self, status_code, context)
