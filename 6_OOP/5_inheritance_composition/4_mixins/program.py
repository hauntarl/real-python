import json

from employees import employee_database, Employee
from payroll import calculate_payroll, LTDPolicy
from productivity import track


def print_dict(d):
    print(json.dumps(d, indent=4))


employees = employee_database.employees

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary')
print_dict(temp_secretary.to_dict())

print('\napplying a long term disability policy to sales employee...')
sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)
