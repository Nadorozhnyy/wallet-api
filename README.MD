# Wallet API
REST приложение которое принимает два запроса вида: 

- POST api/v1/wallets/<WALLET_UUID>/operation

{
operation_type: “DEPOSIT” or “WITHDRAW”,
amount: 1000
}

- GET api/v1/wallets/{WALLET_UUID}

## Для запуска приложения в Docker

## Стек технологий
- Python
- FastAPI
- Postgresql
