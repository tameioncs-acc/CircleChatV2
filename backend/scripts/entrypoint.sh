#!/bin/bash
set -e

echo "Waiting for database..."
while ! nc -z ${DB_HOST:-localhost} ${DB_PORT:-5432}; do
    sleep 1
done
echo "Database is ready!"

echo "Running database migrations..."
alembic upgrade head

echo "Starting server..."
exec uvicorn server.main:app --host 0.0.0.0 --port 8000
