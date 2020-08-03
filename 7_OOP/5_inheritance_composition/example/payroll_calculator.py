from abc import ABC, abstractmethod
import payroll as hr
import employees as emp

salary_employee = emp.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = emp.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = emp.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

try:
    generic_employee = emp.Employee(4, 'Generic Employee')
    payroll_system.calculate_payroll([generic_employee])  # AttributeError
except AttributeError as err:
    print(err)

# The Employee class exists just to be inherited from, not to be instantiated,
# it is called an abstract class, we can't instantiate it but can only inherit
# from it, but here we were able to instantiate the class though it behaves as
# an abstract one, we can restrict this by using a module called 'abc'


# creating an Employee class which inherits from ABC, to make it an abstract
# class
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id,
        self.name = name

    # this annotation forces class inheriting from this to provide an
    # implementation for the given method
    @abstractmethod
    def calculate_payroll(self):
        pass


# if your editor shows errors, you can still run the code to validate output
try:
    print()
    generic_employee = Employee(4, 'Generic Employee')  # TypeError
    payroll_system.calculate_payroll([generic_employee])
except TypeError as err:
    print(err)

# A class that inherits from abstract class with abstract methods must provide
# its own implementation for the abstract methods or should be another abstract
# class within itself, leaving implementation of parent's abstract methods to
# its child class
