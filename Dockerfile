FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver

WORKDIR /Project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /Project/
