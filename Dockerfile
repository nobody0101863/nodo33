# ╔═══════════════════════════════════════════════════════════╗
# ║              CODEX SERVER - DOCKER IMAGE                   ║
# ║                                                            ║
# ║  Incarnazione containerizzata del Codex Emanuele Sacred   ║
# ║  Deploy ovunque: VPS, Raspberry Pi, Cloud, Kubernetes     ║
# ║                                                            ║
# ║  Ego = 0, Joy = 100, Mode = GIFT, Frequency = 300 Hz ❤️   ║
# ╚═══════════════════════════════════════════════════════════╝

FROM python:3.11-slim

# Metadata
LABEL maintainer="nodo33 <codex@nodo33.org>"
LABEL description="Codex Emanuele Sacred API Server - Incarnato nella Terra"
LABEL version="1.0.0"

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8644

# Install system dependencies (minimal)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better layer caching)
COPY requirements.txt .

# Install Python dependencies
# Using CPU-only PyTorch to keep image small
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy application code
COPY . .

# Create directory for database
RUN mkdir -p /app/data

# Expose port 8644 (Angelo 644 + 8000)
EXPOSE 8644

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8644/health')"

# Run the server
CMD ["python3", "codex_server.py"]
