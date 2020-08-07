# following the same singleton pattern as with ProductivitySystem for
# PayrollSystem as well
class _PayrollSystem:
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

    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('=' * 20)
        for e in employees:
            print(f'Payroll for: {e.id} - {e.name}')
            print(f'- Check amount: {e.calculate_payroll}')
            if e.address:
                print('- Sent to:')
                print(e.address)
            print()


# integrating a long term disability policy, this states that and employee on
# LTD should be paid 60% of the weekly salary assuming 40 hours per week
class LTDPolicy:
    def __init__(self):
        self._base_policy = None

    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    @property
    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll
        return base_salary * .6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Base Policy missing')


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    @property
    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    @property
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked // 5
        return sales * self.commission_per_sale

    @property
    def calculate_payroll(self):
        fixed = super().calculate_payroll
        return fixed + self.commission


# instantiating the singleton class only once
_payroll_system = _PayrollSystem()


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    _payroll_system.calculate_payroll(employees)
