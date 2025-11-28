"""
Example test for a student endpoint.

To test your own endpoint:
1. Copy this test function
2. Change the path from "/students/example" to "/students/{your_name}"
3. Change the expected student name to your name
4. Run: pytest tests/test_your_name.py (or just pytest to run all tests)
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_example_student():
    response = client.get("/students/example")
    assert response.status_code == 200
    data = response.json()
    assert data["student"] == "Example Student"
