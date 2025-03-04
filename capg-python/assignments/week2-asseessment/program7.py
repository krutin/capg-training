class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age, employee_id)

    def display_manager_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

    def approve_leave(self, employee_name, days):
        print(f"Leave approved for {employee_name} for {days} days by {self.name} ,Manager.")



person = Person(name="krutin", age=22)
person.display_info()
employee = Employee(name="rishi", age=20, employee_id="asdf1234")
employee.display_employee_info()
manager = Manager(name="shanmukh", age=21, employee_id="qwer1234")
manager.display_manager_info()
manager.approve_leave(employee.name, 5)