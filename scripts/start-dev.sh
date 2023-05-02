#!/usr/bin/env bash
set -e

# Start Uvicorn with live reload
alembic upgrade head
exec uvicorn main:app --reload --reload