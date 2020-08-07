from payroll import get_policy
from productivity import get_role
from contacts import get_employee_address
from representations import AsDictionaryMixin


class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        }

    @property  # this annotation will treat the following method as an instance
    # attribute and not a method which it needs to call, this is possible only
    # if the method does not require any parameters to work
    def employees(self):
        return [Employee(id_) for id_ in self._employees]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(f'invalid employee_id: {employee_id}')
        return info


# Employee now inherits to_dict() method of AsDictionaryMixin which will provide
# dictioanry representation of Employee object
class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(id)
        self.name = info['name']
        self.address = get_employee_address(id)

        # inserting '_' before attribute name to mark it as an internal
        # attribute and should not be included in the dictionary representation
        self._role = get_role(info['role'])
        self._payroll = get_policy(id)

    def work(self, hours):
        duties = self._role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}\n')
        self._payroll.track_work(hours)

    @property
    def calculate_payroll(self):
        return self._payroll.calculate_payroll

    # method added to support the LTDPolicy
    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


# instantiating the singleton class
employee_database = _EmployeeDatabase()
