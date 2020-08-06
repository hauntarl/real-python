from employees import EmployeeDatabase
import json


def print_dict(d):
    print(json.dumps(d, indent=4))


for e in EmployeeDatabase().employees():
    print(e.to_dict())
