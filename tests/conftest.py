
import pytest
from starlette.testclient import TestClient as TestClient
from xawpbe import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
