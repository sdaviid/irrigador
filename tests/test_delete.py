import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


#sprinkler
@pytest.mark.order(4)
def test_delete_sprinkler(test_delete):
    response = test_delete.delete("/sprinkler/1")
    assert response.status_code == 204


@pytest.mark.order(4)
def test_delete_sprinkler_check_was_deleted(test_delete):
    response = test_delete.delete("/sprinkler/1")
    assert response.status_code == 404


@pytest.mark.order(4)
def test_delete_sprinkler_inexist_id(test_delete):
    response = test_delete.delete("/sprinkler/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(4)
def test_delete_sprinkler_wrong_value(test_delete):
    response = test_delete.delete("/sprinkler/wrong")
    assert response.status_code == 422



#plant
@pytest.mark.order(4)
def test_delete_plant(test_delete):
    response = test_delete.delete("/plant/1")
    assert response.status_code == 204


@pytest.mark.order(4)
def test_delete_plant_check_was_deleted(test_delete):
    response = test_delete.delete("/plant/1")
    assert response.status_code == 404


@pytest.mark.order(4)
def test_delete_plant_inexist_id(test_delete):
    response = test_delete.delete("/plant/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(4)
def test_delete_plant_wrong_value(test_delete):
    response = test_delete.delete("/plant/wrong")
    assert response.status_code == 422


#waterday
@pytest.mark.order(4)
def test_delete_waterday(test_delete):
    response = test_delete.delete("/waterday/1")
    assert response.status_code == 204


@pytest.mark.order(4)
def test_delete_waterday_check_was_deleted(test_delete):
    response = test_delete.delete("/waterday/1")
    assert response.status_code == 404


@pytest.mark.order(4)
def test_delete_waterday_inexist_id(test_delete):
    response = test_delete.delete("/waterday/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(4)
def test_delete_waterday_wrong_value(test_delete):
    response = test_delete.delete("/waterday/wrong")
    assert response.status_code == 422