import pytest
import app


@pytest.fixture
def client():
    return app.app.test_client()


def test_health(client):
    res = client.get("/health")

    assert res.text == "ok\n"