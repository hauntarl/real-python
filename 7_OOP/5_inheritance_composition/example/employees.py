class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# --------------Payroll Calculator-------------- #
# this class implicity implements the IPayrollCalculator Interface
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


# this class implicity implements the IPayrollCalculator Interface
class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate


# this class implicity implements the IPayrollCalculator Interface
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# --------------Extension-------------- #
# this class implicitly implements the IWorker interface
class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


# this class implicitly implements the IWorker interface
class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


# this class implicitly implements the IWorker interface
class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


# this class implicitly implements the IWorker interface
class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')
