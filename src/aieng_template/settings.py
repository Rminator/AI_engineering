"""Runtime configuration. Secrets come from the environment, never from code.

On Cloud Run, mount Secret Manager secrets as environment variables:

    gcloud run deploy aieng-template \\
        --set-secrets=SERVICE_API_KEY=my-secret:latest

Locally, export them in your shell. Never commit a real secret.
"""

from __future__ import annotations

import os


def get_service_api_key() -> str | None:
    """API key for the downstream service. None when unset (dev mode)."""
    return os.environ.get("SERVICE_API_KEY")
