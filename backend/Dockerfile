FROM python:3.12-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS=ignore
ENV CURL_CA_BUNDLE=""
ENV POETRY_VIRTUALENVS_CREATE=true
ENV PATH="${PATH}:/root/.local/bin"



WORKDIR /app
COPY . /app/

RUN apt-get update; \
    apt-get install \
        curl \
        git \
        gcc \
    && pip install --no-cache-dir --user poetry==1.7.1 \
    && poetry install --no-interaction --no-ansi \
    && pip install  --no-cache-dir --user requests

RUN ln -sf $(poetry env info -e) /python

RUN poetry run playwright install --with-deps


CMD ["poetry", "run", "uvicorn" "main:app", "--host=0.0.0.0", "--reload"]