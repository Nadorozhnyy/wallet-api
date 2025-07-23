FROM python:3.11.4-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry  \
    && poetry config virtualenvs.create false  \
    && poetry install --no-interaction --no-ansi --no-root

COPY . /app/



