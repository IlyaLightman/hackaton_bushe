FROM python:3.11-slim-buster as python-builder

WORKDIR usr/app/code

RUN apt-get update && apt-get install

RUN pip install --upgrade pip &&  \
    pip install poetry

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false &&  \
    poetry install --no-ansi --no-dev --no-interaction

COPY backend backend
COPY frontend frontend
