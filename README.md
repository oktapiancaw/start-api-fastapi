# start-api-fastapi

FastAPI starter template.

## Quickstart

```bash
uv sync
cp .env.example .env
uv run python -m src.main       # http://127.0.0.1:8000/docs
```

Run all commands from the repo root — `src` is imported as a package from the
working directory (the project is not installed into the venv).

## Layout

```
src/
  configs/      settings (pydantic-settings) + logger setup
  connections/  db / cache / external clients
  middlewares/  ASGI middleware
  models/       pydantic schemas
  routes/v1/    API routers, versioned
  services/v1/  business logic, versioned
  utils/        exceptions and helpers
public/         cache, data, input, output (gitignored contents)
tests/
```

## Adding a route

1. Create `src/routes/v1/<name>.py` with an `APIRouter`.
2. Put logic in `src/services/v1/<name>.py`; keep the route thin.
3. Register it in `src/main.py`: `app.include_router(<name>.router, prefix="/api/v1")`.

Raise `AppError` (or a subclass) from services — the handler in `src/main.py`
turns it into a JSON error response.

## Commands

```bash
uv run pytest
uv run ruff check --fix .
uv run ruff format .
```

## Config

Settings load from env vars and `.env` (`src/configs/env.py`). Add fields to
`ApplicationConfig` and document them in `.env.example`. Nested keys use `__`
(e.g. `DB__HOST`). Logs go to `./logs`.
