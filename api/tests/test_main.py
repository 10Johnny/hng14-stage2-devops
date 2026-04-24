import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_job(monkeypatch):
    fake_redis = MagicMock()
    monkeypatch.setattr(main, "r", fake_redis)
    monkeypatch.setattr(main.uuid, "uuid4", lambda: "test-job-id")

    response = client.post("/jobs")

    assert response.status_code == 200
    assert response.json() == {"job_id": "test-job-id"}
    fake_redis.lpush.assert_called_once_with(main.QUEUE_NAME, "test-job-id")
    fake_redis.hset.assert_called_once_with("job:test-job-id", "status", "queued")


def test_get_job_status(monkeypatch):
    fake_redis = MagicMock()
    fake_redis.hget.return_value = b"completed"
    monkeypatch.setattr(main, "r", fake_redis)

    response = client.get("/jobs/test-job-id")

    assert response.status_code == 200
    assert response.json() == {"job_id": "test-job-id", "status": "completed"}