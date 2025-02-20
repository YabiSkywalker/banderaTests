import json
from http.client import responses
import pytest
import requests

from schemas import authLogin_payload, authRegister_payload, createTicket_payload, default_user

BASE_URL = "https://bandera-svc.yabi.dev"

@pytest.fixture(scope="session")
def test_auth_login():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=authLogin_payload, headers=headers)

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
    response = requests.post(f"{BASE_URL}/auth/register", json=authRegister_payload, headers=headers)
    assert response.status_code == 201
    print(response.text)

def test_create_ticket(test_auth_login):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.post(
        f"{BASE_URL}/tickets/createTicket",
        json=createTicket_payload,
        params=default_user,
        headers=headers
    )
    assert response.status_code == 201
    print(response.json())


#2b45725cfb0142789853df37fc68df9d

