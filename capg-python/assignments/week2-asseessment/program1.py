class Employee:
    def __init__(self, name=None, id=None, department=None):
        self.name = name
        self.id = id
        self.department = department

    def show(self):
        return f"Employee(Name: {self.name}, ID: {self.id}, Department: {self.department})"

employee = Employee()

employee.name = "John Doe"
employee.id = 12345
employee.department = "Engineering"

print(employee.show())