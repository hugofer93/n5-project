FROM python:3.8-alpine3.17

LABEL mantainer="Hugo Silva Álvarez <hugofer93@gmail.com>"

    # Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # Poetry
    POETRY_VERSION=1.3.2 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=1
    # Add Poetry bin to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /opt/n5project

RUN apk add --no-cache gcc g++ linux-headers libffi-dev postgresql-dev \
    && wget -qO- https://install.python-poetry.org | python3 -

COPY . .

RUN poetry install --only main
