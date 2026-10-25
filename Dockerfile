# Phase 0: one Dockerfile you wrote yourself. Every line below should be
# explainable out loud — that is the whole point of this exercise.
FROM python:3.12-slim

# Sane Python defaults inside containers: no .pyc files, unbuffered logs.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /srv/app

# Install uv, then copy ONLY the dependency manifests first. This layer is
# cached until dependencies change, so rebuilds stay fast.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev --no-editable

# Now the code itself.
COPY src ./src

# Drop root: Cloud Run does not require it, and least-privilege is the
# habit to build from day one.
RUN useradd --create-home apprunner && chown -R apprunner /srv/app
USER apprunner

# Cloud Run injects $PORT at deploy time; default to 8080 for local runs.
EXPOSE 8080
CMD ["sh", "-c", "/srv/app/.venv/bin/uvicorn aieng_template.app:app --host 0.0.0.0 --port ${PORT:-8080}"]
