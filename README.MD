# Wallet API
REST приложение которое принимает два запроса вида: 

- POST api/v1/wallets/<WALLET_UUID>/operation

{
operation_type: “DEPOSIT” or “WITHDRAW”,
amount: 1000
}

- GET api/v1/wallets/{WALLET_UUID}

## Для запуска приложения в DOCKER: 
- Заполните .env по примеру из .env.sample
- Если в docker уже имеются контейнеры текущего приложения, то перед запуском необходимо их пересоздать,
удалив при этом старую базу данных
- ````docker-compose up -d````

## Стек технологий
- Python
- FastAPI
- Postgresql