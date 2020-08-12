# as ProductivitySystem class doesn't need to instantiated again and again, we
# can make it a singleton class by following a particular naming convention, i.e
# inserting an underscore before class name to tell the developer that it
# should be used internally and not to be initialized outside this file
class _ProductivitySystem:
    def __init__(self):
        self._role = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._role.get(role_id)
        if not role_type:
            raise ValueError(f'invalid role_id: {role_id}')
        return role_type()

    def track(self, employees, hours):
        print('Tracking employee productivity')
        print('=' * 20)
        for e in employees:
            e.work(hours)
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


# instantiating the singleton class only once and further providing functions
# which can access exposed functionalities of this particular class
_productivity_system = _ProductivitySystem()


def get_role(role_id):
    return _productivity_system.get_role(role_id)


def track(employees, hours):
    _productivity_system.track(employees, hours)
