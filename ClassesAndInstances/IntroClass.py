class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@gmail.com'

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)


emp_1 = Employee('Sadman', 'Soumik', 500000)
emp_2 = Employee('Tamim', 'Iqbal', 100000)

print(emp_1.email)
print(emp_2.email)
print()
print(emp_1.fullName())
print(emp_2.fullName())
print()
print(Employee.fullName(emp_1))  # does the same thing as line 18
print(Employee.fullName(emp_2))  # does the same thing as line 19
