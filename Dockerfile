FROM python:3.12.4-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install --upgrade pip
RUN pip install --upgrade poetry

RUN poetry install --no-dev

COPY src/ ./src

CMD ["poetry", "run", "python", "src/aggregator/main.py"]
