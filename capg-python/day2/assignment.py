def rectangle_area(a,b):
    length = float(a)
    breadth = float(b)
    area = length * breadth
    print(f"Area of the rectangle: {area}")

    
a = input("Enter length of the rectangle: ")
b = input("Enter breadth of the rectangle: ")
rectangle_area(a,b)


def is_prime():
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not prime number.")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            return
    print("Prime number.")

is_prime()



def salary_tax():
    salary = float(input("Enter your annual salary: "))
    
    if salary < 500000:
        tax_rate = 0.10
    else:
        tax_rate = 0.20

    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount

    print(f"Gross Salary: {salary}")
    print(f"Tax Amount: {tax_amount}")
    print(f"Net Salary: {net_salary}")

salary_tax()


def attendance():
    attended = int(input("Enter attended classes: "))
    total = int(input("Enter total classes: "))

    if total == 0:
        print("Total classes cannot be zero.")
        return

    percentage = (attended / total) * 100
    print(f"Attendance Percentage: {percentage:.2f}%")

    if percentage >= 75:
        print("Allowed for the exam.")
    else:
        print("Not allowed for the exam.")

attendance()


import time

def login_system():
    correct_username = "testuser"
    correct_password = "Password@123"
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login Successful!")
            return
        else:
            print("Invalid credentials. Try again.")
            attempts += 1

        if attempts == 3:
            print("Too many failed attempts. Please wait for 2 minutes.")
            time.sleep(120)
            attempts = 0  

login_system()