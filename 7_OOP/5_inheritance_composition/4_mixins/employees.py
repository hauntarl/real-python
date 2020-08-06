from payroll import PayrollSystem
from productivity import ProductivitySystem
from contacts import AddressBook
from representations import AsDictionaryMixin


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.address_book = AddressBook()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.address_book.get_employee_address(id)
        role = self.productivity.get_role(role)
        policy = self.payroll.get_policy(id)
        return Employee(id, name, address, role, policy)


# Employee now inherits to_dict() method of AsDictionaryMixin which will provide
# dictioanry representation of Employee object
class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address

        # inserting '_' before attribute name to mark it as an internal
        # attribute and should not be included in ther dictionary representation
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}\n')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()
