from fastapi.testclient import TestClient

from hello_api.main import app

client = TestClient(app)


def test_hello_without_name_greets_world() -> None:
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_hello_with_name_greets_that_name() -> None:
    response = client.get("/hello", params={"name": "JS"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, JS!"}
