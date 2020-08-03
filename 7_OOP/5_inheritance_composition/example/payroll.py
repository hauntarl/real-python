# a class that conforms to IPayrollCalculator interface from the UML diagrom
# can be used in calculate_payroll() of the PayrollSystem
# UML: https://files.realpython.com/media/ic-initial-employee-inheritance.b5f1e65cb8d1.jpg
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
