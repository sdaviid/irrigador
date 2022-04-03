import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


#sprinkler
@pytest.mark.order(2)
def test_get_sprinkler(test_read):
    response = test_read.get("/sprinkler/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_sprinkler_inexist_id(test_read):
    response = test_read.get("/sprinkler/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_sprinkler_wrong_value(test_read):
    response = test_read.get("/sprinkler/asd")
    assert response.status_code == 422


#plant
@pytest.mark.order(2)
def test_get_plant(test_read):
    response = test_read.get("/plant/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_plant_inexist_id(test_read):
    response = test_read.get("/plant/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_plant_wrong_value(test_read):
    response = test_read.get("/plant/asd")
    assert response.status_code == 422


#waterday
@pytest.mark.order(2)
def test_get_waterday(test_read):
    response = test_read.get("/waterday/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_waterday_inexist_id(test_read):
    response = test_read.get("/waterday/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_waterday_wrong_value(test_read):
    response = test_read.get("/waterday/asd")
    assert response.status_code == 422


#log
@pytest.mark.order(2)
def test_get_log(test_read):
    response = test_read.get("/log/1")
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_log_inexist_id(test_read):
    response = test_read.get("/log/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Don't find ID specified"


@pytest.mark.order(2)
def test_get_log_wrong_value(test_read):
    response = test_read.get("/log/asd")
    assert response.status_code == 422