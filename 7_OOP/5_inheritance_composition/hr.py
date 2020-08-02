# these classes are structured according to the UML diagram
# https://files.realpython.com/media/ic-initial-employee-inheritance.b5f1e65cb8d1.jpg


class PayrollSystem:
    # calculate_payroll accepts a list of employees which conceptually
    # implements the IPayrollCalculator interface
    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('=' * 20)
        for e in employees:
            print(f'Payroll for: {e.id} - {e.name}')
            print(f'- Check amount: {e.calculate_payroll()}')
            print()


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    # NOTE: if we do not explicity create the __init__ method for a class then
    # it automatically inherit everything from the parent, but we do define an
    # __init__ then it covers up all of the instance attributes in the parent
    # and we must set them manually by calling the __init__ method of the parent
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
