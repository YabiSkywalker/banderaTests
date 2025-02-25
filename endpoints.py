from pydantic import BaseModel, Field


##########################################
BASE_URL = "https://bandera-svc.yabi.dev"
##########################################

##########################################
AUTH_CONTROLLER = "auth"
##########################################

##########################################
TICKET_CONTROLLER = "tickets"
##########################################

##########################################
CUSTOMER_CONTROLLER = "customers"
##########################################

##########################################
EMPLOYEES_CONTROLLER = "employees"
##########################################

##########################################
BILLING_CONTROLLER = "billing"
##########################################

##########################################
QUERY_CONTROLLER = "query"
##########################################


# Authentication Controller
login_endpoint = "{AUTH_CONTROLLER}/login"
register_endpoint = "{AUTH_CONTROLLER}/register"


# Ticket Controller
create_ticket_endpoint = "tickets/createTicket"
set_status_endpoint = "tickets/{id}/setStatus"
set_appointment_endpoint = "tickets/{id}/setAppointment"
add_services_endpoint = "tickets/{id}/addServices"
update_assignee_endpoint = "tickets/updateAssignee"
find_ticket_by_id_endpoint = "/tickets"
get_all_tickets_endpoint = "/tickets"
delete_ticket_endpoint = "/tickets/{id}/delete"
delete_service = "/tickets/{id}/removeSerivces"  # Ex: "/tickets/{id}/removeServices?index=1"

# Customer Controller
add_new_customer_endpoint = ""



# Billing Controller

# Employees Controller
get_all_employees_endpoint = "employees/getAllEmployees"
# Query Contoller

