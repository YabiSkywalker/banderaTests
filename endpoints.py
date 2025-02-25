from pydantic import BaseModel, Field




#Controllers
AUTH_CONTROLLER = "auth"
TICKET_CONTROLLER = "tickets"
CUSTOMER_CONTROLLER = "customers"
EMPLOYEES_CONTROLLER = "employees"
BILLING_CONTROLLER = "billing"
QUERY_CONTROLLER = "query"

#Environment vars
SUB_DOMAIN = "bandera-svc"
DOMAIN = "yabi.dev"
BASE_URL = "https://{SUB_DOMAIN}.{DOMAIN}"

####################################################################################
###################### AUTHENTICATION CONTROLLER ENDPOINTS #########################
####################################################################################
login_endpoint = "{AUTH_CONTROLLER}/login"
register_endpoint = "{AUTH_CONTROLLER}/register"

#Ex: ----> https://{SUB_DOMAIN}.{DOMAIN}/{login_endpoint}


####################################################################################
########################## TICKET CONTROLLER ENDPOINTS #############################
####################################################################################
create_ticket_endpoint = "{TICKET_CONTROLLER}/createTicket"
set_status_endpoint = "{TICKET_CONTROLLER}/{id}/setStatus"
set_appointment_endpoint = "{TICKET_CONTROLLER}/{id}/setAppointment"
add_services_endpoint = "{TICKET_CONTROLLER}/{id}/addServices"
update_assignee_endpoint = "{TICKET_CONTROLLER}/updateAssignee"
find_ticket_by_id_endpoint = "{TICKET_CONTROLLER}"
get_all_tickets_endpoint = "{TICKET_CONTROLLER}"
delete_ticket_endpoint = "{TICKET_CONTROLLER}/{id}/delete"
delete_service = "{TICKET_CONTROLLER}/{id}/removeServices"  # Ex: "/tickets/{id}/removeServices?index=1"




####################################################################################
######################### CUSTOMER CONTROLLER ENDPOINTS ############################
####################################################################################
add_new_customer_endpoint = "{CUSTOMER_CONTROLLER}/addNewCustomer"
update_customer_info_endpoint = "{CUSTOMER_CONTROLLER}/{id}/update"
get_customer_by_id_endpoint = "{CUSTOMER_CONTROLLER}/{id}"
get_all_customers_endpoint = "{CUSTOMER_CONTROLLER}/getAllCustomers"
delete_customer_endpoint = "{CUSTOMER_CONTROLLER}/{id}/delete"





####################################################################################
######################### BILLING CONTROLLER ENDPOINTS #############################
####################################################################################
reconciler_endpoint = "{BILLING_CONTROLLER}/reconcile/{id]"




####################################################################################
######################### EMPLOYEES CONTROLLER ENDPOINTS ###########################
####################################################################################
get_all_employees_endpoint = "{EMPLOYEES_CONTROLLER}/getAllEmployees"
get_employee_by_id_endpoint = "{EMPLOYEES_CONTROLLER}/{id}"
delete_employee_endpoint = "{EMPLOYEES_CONTROLLER}/{id}/delete"
update_employee_info_endpoint = "{EMPLOYEES_CONTROLLER}/{id}/update"




####################################################################################
########################## QUERY CONTROLLER ENDPOINTS ##############################
####################################################################################
service_hist_by_vin_endpoint = "{QUERY_CONTROLLER}/service-history/{vin}"
find_all_customer_cars_endpoint = "{QUERY_CONTROLLER}/owner/{customerId}"
query_assigned_by_employee_id_endpoint = "{QUERY_CONTROLLER}/assignee/{employeeId}"


