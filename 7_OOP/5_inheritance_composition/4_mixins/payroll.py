class PayrollSystem:
    # ----------COMPOSITION---------- #
    # __init__ and get_policy mocks the database for payment policy associated
    # with each Employee
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError(f'invalid employee_id: {employee_id}')
        return policy
    # ----------COMPOSITION---------- #

    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('=' * 20)
        for e in employees:
            print(f'Payroll for: {e.id} - {e.name}')
            print(f'- Check amount: {e.calculate_payroll()}')

            # ----------COMPOSITION---------- #
            if e.address:
                print('- Sent to:')
                print(e.address)
            # ----------COMPOSITION---------- #

            print()


# ----------COMPOSITION---------- #
class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours
# ----------COMPOSITION---------- #


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    # ----------COMPOSITION---------- #
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked // 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission()
    # ----------COMPOSITION---------- #
