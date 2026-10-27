from fastapi.testclient import TestClient

from src.main import app
from src.utils.exceptions import NotFoundError

client = TestClient(app)


def test_health():
    res = client.get("/api/v1/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_app_error_handler():
    @app.get("/_boom")
    async def boom():
        raise NotFoundError("nope")

    res = TestClient(app, raise_server_exceptions=False).get("/_boom")
    assert res.status_code == 404
    assert res.json() == {"error": "NotFoundError", "message": "nope"}
