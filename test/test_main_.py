from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert "Cloud Security Dashboard" in response.text


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "cloud-security-app"


def test_status():
    response = client.get("/api/status")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "cloud-security-dashboard"
    assert data["status"] == "running"


def test_security():
    response = client.get("/api/security")

    assert response.status_code == 200

    data = response.json()

    assert data["security_status"] == "secure"
    assert data["https"] is True


def test_deployment():
    response = client.get("/api/deployment")

    assert response.status_code == 200

    data = response.json()

    assert data["pipeline"] == "GitHub Actions"
    assert data["container"] == "Docker"
    assert data["platform"] == "AWS"