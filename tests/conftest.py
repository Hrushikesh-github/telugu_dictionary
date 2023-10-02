import pytest
from starlette.testclient import TestClient
from app import main
from app.db_connection import connect_db


@pytest.fixture(scope="module")
def test_app():
    # set up
    with TestClient(main.app) as test_client:
        # testing
        yield test_client

@pytest.fixture(scope="module")
def test_db():
    db_connection = connect_db()
    yield db_connection