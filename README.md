# aieng-template — Phase 0 repo template

Starter scaffold for **Phase 0 (Engineering baseline, Weeks 1–2, Oct 19 – Nov 1)** of the
24-week AI Engineering Capability Plan. It implements every Phase 0 requirement:

| Requirement            | Where it lives                          |
|------------------------|-----------------------------------------|
| `uv` project layout    | `pyproject.toml`, `.python-version`     |
| `ruff` lint + format   | `[tool.ruff]` in `pyproject.toml`       |
| Type hints, enforced   | `mypy` (`disallow_untyped_defs`)        |
| `pytest`               | `tests/test_app.py`                     |
| Self-written Dockerfile| `Dockerfile` (commented line by line)   |
| GitHub Actions on PR   | `.github/workflows/ci.yml`             |
| Secret Manager pattern | `src/aieng_template/settings.py`        |

## Weekend setup (before Monday Oct 19)

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create the GitHub repo, then clone it and drop these files in

# 3. Sync + verify locally
uv sync
uv run ruff check . && uv run ruff format --check .
uv run mypy src
uv run pytest

# 4. Run the service locally
uv run uvicorn aieng_template.app:app --reload
# -> http://127.0.0.1:8000/health
```

## Deploy to Cloud Run

```bash
# One-time: enable the APIs and create the secret
gcloud services enable run.googleapis.com secretmanager.googleapis.com
echo -n "replace-me" | gcloud secrets create my-secret --data-file=-

# Build + deploy (secret mounted as an env var)
gcloud run deploy aieng-template \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-secrets=SERVICE_API_KEY=my-secret:latest
```

## Phase 0 gate

Before moving to Phase 1, be able to explain — without condescending to a data
scientist — **why a notebook isn't a deployment artifact.**

Prompts to pressure-test yourself:

- What happens to a notebook's hidden cell-execution order the day someone re-runs it?
- Where do its dependencies live, and who pins them?
- How do you roll a notebook back at 2am? How do you roll *this* back?
- What does the Dockerfile know that the notebook never writes down?
- If the model behavior changes, which artifact tells you *what code* was running?

Suggested rewrite exercise for Week 2: delete this Dockerfile and write it again
from memory. If you can, the baseline is yours.
