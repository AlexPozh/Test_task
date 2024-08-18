from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_query_endpoint():
    response = client.get("/query", params={"cadastral_num": "123.123"})
    assert response.status_code == 200
    assert isinstance(response.json()['server_answer'], bool)


def test_ping_endpoint():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is active."}


def test_history_endpoint():
    response = client.get("/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
