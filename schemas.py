# schemas.py
from dataclasses import Field

from pydantic import BaseModel

#Min ref data
default_user = {
    "employeeId": "6764b549dfcd976d834c27d9" # This can be passed in the request URL like ?userId=123
}
###############################################

authLogin_payload = {
    "email": "test@example.com",
    "password": "password123"
}

authRegister_payload = {
    "firstName": "Zen",
    "lastName": "Skywalker",
    "phoneNumber": "773-804-8920",
    "address": "2353 W Congress Parkway Unit 2 Chicago, IL 60612",
    "email": "zen@skywalkerlabs.com",
    "password": "password123"
}

createTicket_payload = {
    "dateTime": "2025-02-15 12:35 AM",
    "services": [
        {
            "serviceType": "Engine",
            "serviceDetails": "Oil Change",
            "partsRequired": [
                {
                    "partName": "5w30",
                    "partQty": 6,
                    "partPrice": 15
                },
                {
                    "partName": "Filter OEM",
                    "partQty": 1,
                    "partPrice": 12
                }
            ]
        }
    ],
    "preliminaryCost": 90,
    "tax": 13,
    "subtotal": 115.26,
    "ticketStatus": "INIT",
    "customer": {
        "firstName": "New",
        "lastName": "Customer",
        "phoneNumber": "1 312 123 1234",
        "email": "new@customer.com"
    },
    "vehicle": {
        "year": 2012,
        "make": "Honda",
        "model": "Accord",
        "vin": "VDSF5485451DSAF4"
    }
}

addServices_payload = {
  "serviceType": "Engine",
  "serviceDetails": "Ignition Coils",
  "partsRequired": [
    {
      "partName": "Coil Pack",
      "partQty": 6,
      "partPrice": 55
    },
    {
      "partName": "Misc",
      "partQty": 4,
      "partPrice": 12
    }
  ]
}


