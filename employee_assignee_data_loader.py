from faker import Faker
from schemas import auth_register_payload

faker = Faker()


def create_employee_group():
    employee_group = []
    for _ in range(20):
        employee_group.append(auth_register_payload())
    return employee_group

# test to ensure correct data is generated
# employee_group = create_employee_group()
# for employee in employee_group:
#    print(employee)
