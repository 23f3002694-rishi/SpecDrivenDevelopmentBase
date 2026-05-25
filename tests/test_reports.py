from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_report_found():

    response = client.get("/reports/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    assert "internal_id" not in data

    assert "owner_email" not in data


def test_get_report_missing():

    response = client.get("/reports/99999")

    assert response.status_code == 404

    assert response.json()["detail"] == "Report not found"