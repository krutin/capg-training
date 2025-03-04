

class Student:
    def __init__(self,name = None, roll_no = None):
        self.name = name
        self.roll_no = roll_no
    
    def show(self):
        print(f'student Name : {self.name}, roll_no: {self.roll_no}')


std = Student('rishi',89)

std.show()