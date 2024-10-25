FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "src.main:app", "--reload"]