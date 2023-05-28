from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)

def test_get_infos():
    response = client.get("/")
    assert response.status_code == 200
