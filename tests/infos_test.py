from starlette.testclient import TestClient
from app.models.umng_info import Info
from app.main import app

client = TestClient(app)


def test_get_infos():
    response = client.get('/api/v1/infos')
    assert response.status_code == 200


def test_post_info():
    """
    In this test, for each running new record is adding in database
    It is not a desired behaviour
    """
    response = client.post("/api/v1/infos",
                           headers={"X-Token": "coneofsilence"},
                           json={"info": "A test","last_update": "Today","author": "Me"})
    assert response.status_code == 200
    assert response.json() == "Information added"


def test_update_info():
    id = "123aaab9697a24204fc44ea5"
    response = client.put(f"/api/v1/infos/{id}",
                        headers={"X-Token": "coneofsilence"},
                        json={"info": "A test", "last_update": "Today", "author": "Me"})
    assert response.status_code == 200


def test_delete_info():
    id="123aaab9697a24204fc44ea5"
    response=client.delete(f"/api/v1/infos/{id}")
    assert response.status_code == 200
    assert response.json() == "Information successfully deleted"

