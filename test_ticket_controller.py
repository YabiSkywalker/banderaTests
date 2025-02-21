from http.client import responses

import pytest
from pydantic import BaseModel, Field
import requests

from PythonProject.endpoints import update_assignee_endpoint, get_all_employees_endpoint
from schemas import createTicket_payload, default_user, addServices_payload
from endpoints import BASE_URL, create_ticket_endpoint, set_status_endpoint, set_appointment_endpoint, \
    add_services_endpoint
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
        f"{BASE_URL}/{set_status_endpoint}",
        headers=headers,
        params = {
            "id" : test_create_ticket,
            "status" : "OPEN"
        }
    )
    assert response.status_code == 200  # Adjust based on expected status code
    print(response.text)

def test_add_services(test_auth_login, test_create_ticket):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    format_endpoint = add_services_endpoint.format(id=test_create_ticket)
    response = requests.patch(
        f"{BASE_URL}/{format_endpoint}",
        headers=headers,
        params=test_create_ticket,
        json=addServices_payload
    )
    assert response.status_code == 200
    print(response.text, response.json(), response)

def test_update_assignee(test_auth_login, test_create_ticket):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {test_auth_login}"
    }
    response = requests.get(
        f"{BASE_URL}/{get_all_employees_endpoint}",
        headers=headers
    )
    employee_list = response.json()
    second_employee = employee_list[1]
    second_employee_id = second_employee.get("id")

    assert response.status_code == 200
    print(response.text, response.json(), response)

    #url = f"{BASE_URL}/{update_assignee_endpoint}/{test_create_ticket}"
    response = requests.patch(
        f"{BASE_URL}/{update_assignee_endpoint}/{test_create_ticket}",
        headers=headers,
        params = {
            "employeeId" : second_employee_id
        }
    )

    assert response.status_code == 200
    print(response.text, response.json(), response)