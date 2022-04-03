import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_create():
    client = TestClient(app)
    yield client 


@pytest.fixture(scope="module")
def test_read():
    client = TestClient(app)
    yield client 


@pytest.fixture(scope="module")
def test_update():
    client = TestClient(app)
    yield client 


@pytest.fixture(scope="module")
def test_delete():
    client = TestClient(app)
    yield client 