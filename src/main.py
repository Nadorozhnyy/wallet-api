from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.exceptions.handle_http_exceptions import (
    handle_api_exceptions,
    handle_internal_exception,
)
from src.exceptions.base import BaseAPIException
from src.routes import api_router
from src.settings import SETTINGS

app = FastAPI(title="Wallet")

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(BaseAPIException, handle_api_exceptions)
app.add_exception_handler(Exception, handle_internal_exception)
app.include_router(router=api_router, prefix=SETTINGS.API_V1_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
