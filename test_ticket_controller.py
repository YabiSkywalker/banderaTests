import pytest
from pydantic import BaseModel, Field
import requests

from schemas import createTicket_payload, default_user
from endpoints import BASE_URL, create_ticket_endpoint, set_status_endpoint, set_appointment_endpoint
from test_authentication_Controller import test_auth_login

@pytest.fixture(scope="session")
def test_create_ticket(test_auth_login):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.post(
        f"{BASE_URL}/{create_ticket_endpoint}",
        json=createTicket_payload,
        params=default_user,
        headers=headers
    )
    assert response.status_code == 201
    ticket_id = response.json().get("id")
    print(response.json())
    return ticket_id

##############################################
### Skipping /tickets/updateCosts for now ####
##############################################


def test_set_status(test_auth_login, test_create_ticket):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params = {
            "id" : test_create_ticket,
            "status" : "OPEN"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "PEND"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "ACTIV"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "LATE"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "DONE"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "DUE"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "PAID"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

    response = requests.patch(
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params={
            "id": test_create_ticket,
            "status": "VOID"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)
    ticket_id = response.json().get("id")
    return ticket_id



def test_set_appointment(test_auth_login, test_create_ticket):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.patch(
        f"{BASE_URL}/{set_appointment_endpoint}",
        headers=headers,
        params = {
            "id" : test_create_ticket,
            "dateTime" : "2025-06-12 11:35 PM"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

