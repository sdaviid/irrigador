import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


#sprinkler
@pytest.mark.order(2)
def test_get_sprinkler(test_read):
    response = test_read.get("/sprinkler/get/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_sprinkler_inexist_id(test_read):
    response = test_read.get("/sprinkler/get/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_sprinkler_wrong_value(test_read):
    response = test_read.get("/sprinkler/get/asd")
    assert response.status_code == 422


#plant
@pytest.mark.order(2)
def test_get_plant(test_read):
    response = test_read.get("/plant/get/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_plant_inexist_id(test_read):
    response = test_read.get("/plant/get/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_plant_wrong_value(test_read):
    response = test_read.get("/plant/get/asd")
    assert response.status_code == 422


#waterday
@pytest.mark.order(2)
def test_get_waterday(test_read):
    response = test_read.get("/waterday/get/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_waterday_inexist_id(test_read):
    response = test_read.get("/waterday/get/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_waterday_wrong_value(test_read):
    response = test_read.get("/waterday/get/asd")
    assert response.status_code == 422


#log
@pytest.mark.order(2)
def test_get_log(test_read):
    response = test_read.get("/log/get/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_log_inexist_id(test_read):
    response = test_read.get("/log/get/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_log_wrong_value(test_read):
    response = test_read.get("/log/get/asd")
    assert response.status_code == 422