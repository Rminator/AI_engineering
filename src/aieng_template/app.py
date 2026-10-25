"""Minimal HTTP service for the Phase 0 template.

Two routes, fully typed, fully tested:

* ``GET /``       — service identity
* ``GET /health`` — liveness probe for Cloud Run
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from aieng_template.settings import get_service_api_key

app = FastAPI(title="aieng-template")


@app.get("/")
def index() -> dict[str, str]:
    return {"service": "aieng-template", "phase": "0"}


@app.get("/health")
def health() -> JSONResponse:
    configured = get_service_api_key() is not None
    return JSONResponse({"ok": True, "secrets_configured": configured})
