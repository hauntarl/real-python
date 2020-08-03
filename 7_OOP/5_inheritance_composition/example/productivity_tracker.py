import employees as emp
import productivity as ps
import payroll as hr

manager = emp.Manager(1, 'John Smith', 1500)
secretary = emp.Secretary(2, 'Jane Doe', 1200)
sales_guy = emp.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = emp.FactoryWorker(4, 'Pete Peterson', 40, 15)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]

productivity_system = ps.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
