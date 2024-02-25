# syntax=docker/dockerfile:1

# Base Image
ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working Directory
WORKDIR /app

# Non-Privileged User
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Python Dependencies
# Note: The requirements.txt file must include Flask, flask_swagger_ui, gunicorn, etc.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application Code
COPY . .

# Use the Non-Privileged User
USER appuser

# Expose the Correct Port (Align with Flask App)
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]