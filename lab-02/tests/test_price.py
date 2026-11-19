import pytest
import requests
import responses as responses_lib
import app

PARTNER_URL = "http://partner.net"


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setattr(app, "PARTNER_URL", PARTNER_URL)
    return app.app.test_client()
    

@responses_lib.activate
def test_partner_called_once(client):
    responses_lib.get(f"{PARTNER_URL}/v1/catalog/MK-II", json={"price": "1", "currency": "UAH"})
    
    client.get("/price/MK-II")
    
    assert len(responses_lib.calls) == 1
    assert responses_lib.calls[0].request.url == f"{PARTNER_URL}/v1/catalog/MK-II"
    

@pytest.mark.parametrize("mock_kwargs, expected_error", [
    ({"status": 500}, "HTTPError"),
    ({"body": requests.exceptions.Timeout()}, "Timeout")
])
@responses_lib.activate
def test_partner_failures(client, mock_kwargs, expected_error):
    responses_lib.get(f"{PARTNER_URL}/v1/catalog/MK-II", **mock_kwargs)
    
    resp = client.get("/price/MK-II")
    
    assert resp.status_code == 502
    assert resp.get_json()["error"] == expected_error
