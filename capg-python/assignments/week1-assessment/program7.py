def check_loan(salary,age,credit_score):
    if(age < 18 or credit_score < 600):
        return "not approved. credit score low"
    elif(salary < 50000):
        return "not approved. salary too low"
    else:
        return "Loan Approved!"

salary = int(input("enter salary:"))
age = int(input("enter age:"))
credit_score = int(input("Enter credit score:"))

print(check_loan(salary, age, credit_score))
