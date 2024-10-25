# Dockerfile
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Configure Poetry to not use virtual environments within the container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
