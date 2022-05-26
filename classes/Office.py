import Employee


class Office:
    def __init__(self, name):
        self._name = name
        self._employees = []

    def get_all_emp(self):
        return self._employees

    def get_employee(self, emp_id):
        employee = list(filter(lambda emp: emp.id == emp_id, self._employees))
        if len(employee) == 0:
            return None
        return employee[0]

    def hire(self, employee: Employee):
        self._employees.append(employee)

    def fire(self, emp_id):
        self._employees.remove(self.get_employee(emp_id))
