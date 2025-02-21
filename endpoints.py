from pydantic import BaseModel, Field


##########################################
BASE_URL = "https://bandera-svc.yabi.dev"
##########################################


# Authentication Controller
login_endpoint = "auth/login"
register_endpoint = "auth/register"


# Ticket Controller
create_ticket_endpoint = "tickets/createTicket"
set_status_endpoint = "tickets/{id}/setStatus"
set_appointment_endpoint = "tickets/{id}/setAppointment"
add_services_endpoint = "tickets/{id}/addServices"
update_assignee_endpoint = "tickets/updateAssignee"

# Customer Controller

# Billing Controller

# Employees Controller
get_all_employees_endpoint = "employees/getAllEmployees"
# Query Contoller

