class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# --------------Payroll Calculator-------------- #
# this class implicity implements the IPayrollCalculator Interface
class SalaryEmployee(Employee):
    # NOTE: if we do not explicity create the __init__ method for a class then
    # it automatically inherit everything from the parent, but we do define an
    # __init__ then it covers all of the instance attributes in the parent and
    # we must set them manually by calling the __init__ method of the parent
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# this class implicity implements the IPayrollCalculator Interface
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


# this class implicity implements the IPayrollCalculator Interface
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# --------------Productivity Tracker-------------- #
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


# --------------The Diamond Problem-------------- #
# UML: https://files.realpython.com/media/ic-diamond-problem.8e685f12d3c2.jpg
class TemporarySecretary(Secretary, HourlyEmployee):
    # we need to explicitly define the __init__ method for TemporarySecretary to
    # avoid any issues initializing the super class, if we do not provide, then
    # Python will look for __init__ method of its super class, ordered by MRO.
    # As Secretary doesn't have any __init__ method, it will search in its super
    # class which is SalaryEmployee, which requires 3 parameters but we are
    # passing 4, so Python raises an exception. Even if we switch up the order
    # using TemporarySecretary(HourlyEmployee, Secretary) signature,
    # HourlyEmployee makes a super().__init__() call with only 2 parameters,
    # assuming it will initialize the Employee class, but instead Python tries
    # to initialize the Secretary class which delegates the call to
    # SalaryEmployee, which requires 3 paramters but only receives 2 and raises
    # an Exception.
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
        # by defining __init__ method and explicity initializing only a
        # particular super class which we require, we tackle the issue

    # another issue rises when we try to call calculate_payroll() method, here
    # both Secretary via SalaryEmployee and HourlyEmployee provide the
    # implementation for this method, Python traverses the MRO from left until
    # it finds the first super class which provides the implementation for it.
    # which here is SalaryEmployee and requires weekly_salary attribute hence
    # raises another exception. In order to resolve this issue, we need to
    # define calculate_payroll() for TemporarySecretary class.
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


# This is an example of a diamond problem, when you inherit from 2 or more
# classes and they share the same ancestor, MRO determines the search order for
# parent classes. This can get pretty messy and the only way we could fix it was
# with a sort of patch on our TemporarySecretary class, even then we had to be
# careful, when you see a diamond, typically it is a time to rethink your design
