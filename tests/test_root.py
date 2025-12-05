from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    # Root endpoint returns HTML, not JSON
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    html_content = response.text
    assert "Python Workshop API" in html_content
    assert "Student" in html_content
