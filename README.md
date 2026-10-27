# start-api-fastapi

Cookiecutter template for a FastAPI service.

## Generate a project

```bash
uvx cookiecutter gh:oktapiancaw/start-api-fastapi
# or from a local clone:
uvx cookiecutter path/to/start-api-fastapi
```

Prompts collected:

| Variable              | Default           |
| --------------------- | ----------------- |
| `project_name`        | `My API`          |
| `project_slug`        | derived from name |
| `package_description` | `A FastAPI service` |
| `author_name`         | `Your Name`       |
| `author_email`        | `you@example.com` |
| `python_version`      | `3.12`            |
| `http_host`           | `127.0.0.1`       |
| `http_port`           | `8000`            |

After generation, the post-gen hook runs `git init` and prints the next
commands.

## Layout shipped to the generated project

```
<project_slug>/
  pyproject.toml
  .env.example
  .python-version
  README.md
  src/
    configs/      pydantic-settings + logger
    connections/  db / cache / external clients
    middlewares/  ASGI middleware
    models/       pydantic schemas
    routes/v1/    versioned API routers (sample: health)
    services/v1/  versioned business logic
    utils/        exceptions and helpers
    main.py
  public/{cache,data,input,output}/
  tests/
  logs/
```

See the generated project's own `README.md` for day-to-day commands.
