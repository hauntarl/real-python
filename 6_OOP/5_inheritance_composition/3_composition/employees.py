from payroll import PayrollSystem
from productivity import ProductivitySystem
from contacts import AddressBook


# ----------COMPOSITION---------- #
# this class mocks the database for Employees
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
# ----------COMPOSITION---------- #


class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name

        # ----------COMPOSITION---------- #
        # Employee is loosely coupled with the Address class, adding address
        # as an attribute of the Employee class means Employee is composed of
        # Address (Employee 'has-a' Address)
        self.address = address
        self.role = role
        self.payroll = payroll
        # ----------COMPOSITION---------- #

    # ----------COMPOSITION---------- #
    def work(self, hours):
        duties = self.role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}\n')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
    # ----------COMPOSITION---------- #
