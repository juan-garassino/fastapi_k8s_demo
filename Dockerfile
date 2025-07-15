FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .[uvicorn]

# Copy source code
COPY src/ /app/src/

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]