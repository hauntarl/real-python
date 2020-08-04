class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking employee productivity')
        print('=' * 20)
        for e in employees:
            result = e.work(hours)
            print(f'{e.name}: {result}')
        print()


class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing office paperwork.'


class SalesRole:
    def work(self, hours):
        return f'expends {hours} hours on phone.'


class FactoryRole:
    def work(self, hours):
        return f'manufactures gadgets for {hours} hours.'
