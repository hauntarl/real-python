import employees as emp
import productivity as ps
import payroll as hr


print(emp.TemporarySecretary.__mro__, '\n')
temp_secretary = emp.TemporarySecretary(5, 'Robin Williamson', 40, 9)

employees = [temp_secretary]

productivity_system = ps.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
