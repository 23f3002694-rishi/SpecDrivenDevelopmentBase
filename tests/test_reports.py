from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_report_found():

    reports = client.get("/reports").json()["items"]

    existing_id = reports[0]["id"]

    response = client.get(f"/reports/{existing_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == existing_id

    assert "internal_id" not in data

    assert "owner_email" not in data


def test_get_report_missing():

    reports = client.get("/reports").json()["items"]

    missing_id = max(r["id"] for r in reports) + 1

    response = client.get(f"/reports/{missing_id}")

    assert response.status_code == 404

    assert response.json()["detail"] == "Report not found"