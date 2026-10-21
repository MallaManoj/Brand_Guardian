# ==============================================================================
# Brand Guardian AI - Container Image
# ==============================================================================
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system dependencies including ffmpeg for yt-dlp media extraction
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ffmpeg \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency configuration
COPY pyproject.toml uv.lock* /app/

# Install uv package manager and dependencies
RUN pip install --no-cache-dir uv && \
    uv pip install --system -r pyproject.toml

# Copy project source code
COPY backend/ /app/backend/
COPY main.py /app/main.py

# Expose FastAPI service port
EXPOSE 8000

# Health check to ensure API responsiveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Launch FastAPI ASGI server
CMD ["uvicorn", "backend.src.api.server:app", "--host", "0.0.0.0", "--port", "8000"]
