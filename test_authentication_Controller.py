import json
from http.client import responses
import pytest
import requests

from schemas import authLogin_payload, authRegister_payload, createTicket_payload, default_user
from endpoints import BASE_URL, login_endpoint, register_endpoint

@pytest.fixture(scope="session")
def test_auth_login():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(f"{BASE_URL}/{login_endpoint}", json=authLogin_payload, headers=headers)

    assert response.status_code == 200, "Failed JWT Authentication"
    assert "id" in response.json()
    assert "token" in response.json(), "Token not found"
    token = response.json().get("token")
    id = response.json().get("id")
    print(response.json())
    return token

def test_auth_register(test_auth_login):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.post(f"{BASE_URL}/{register_endpoint}", json=authRegister_payload, headers=headers)
    assert response.status_code == 201
    print(response.text)



#2b45725cfb0142789853df37fc68df9d

