from datetime import datetime
from util import ran


class Employee:

    def __init__(self, name, age: int, service: int, employee_id: int):
        self.name = name
        self.age = age
        self.service = service
        self.__employee_id = employee_id

    def showinfo(self):
        print(f'{self.__class__} Name : {self.name}\n\t Age: {self.age}\n\t Service: '
              f'{self.service} years\n\t Id: {self.__employee_id}')


class Manager(Employee):
    def __init__(self, name, age, service, employee_id):
        super().__init__(name, age, service, employee_id)


class Staff(Employee):
    def __init__(self, name, age, service, employee_id):
        super().__init__(name, age, service, employee_id)


class Engineer(Employee):
    def __init__(self, name, age, service, employee_id):
        super().__init__(name, age, service, employee_id)


while True:
    def make_class(name, age, service, employee_id):
        emp_name = input('Input your name: ')
        emp_age = int(input('Input your age: '))
        emp_service = int(input('Input year you start working: '))
        emp_employeeid = int(input('Input your employee id number: '))
        Employee(emp_name, emp_age, emp_service, employee_id)

        

