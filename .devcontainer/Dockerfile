FROM python:3.10-slim

# Vereiste system packages installeren
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    build-essential \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    python3-dev

# Werkdirectory instellen
WORKDIR /workspace
