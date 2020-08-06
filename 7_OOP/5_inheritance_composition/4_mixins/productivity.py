class ProductivitySystem:
    # ----------COMPOSITION---------- #
    # __init__ and get_role mocks the database for types of Employees
    def __init__(self):
        # NOTE: the underscore befor the 'role' attribute is to tell the
        # developer that they shouldn't directly access this attribute from
        # outside the class, instead this class utilizes this field in one of
        # its methods.
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
    # ----------COMPOSITION---------- #

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
