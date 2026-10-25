"""Smoke tests for the Phase 0 template service."""

from __future__ import annotations

from fastapi.testclient import TestClient

from aieng_template.app import app

client = TestClient(app)


def test_index_returns_service_identity() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "aieng-template"


def test_health_reports_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["ok"] is True
