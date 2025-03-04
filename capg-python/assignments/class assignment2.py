# we're building a system to represent various types of employees in a company. 
# All employees have some common attributes (like name, age, and salary), but different types of employees might have specific behaviors or additional attributes
# (like managers having departments, and engineers having special skills).

# a) take input from the user about employee details minimum 3 employees in every department
# b) find who is the manager for give department
# c) how many employees working in that given department
# d) take input as skill how many engineers have that give skill 
# e) print total employee in every department
# f) print total employees in all departments 


class Employee:
    def __init__(self):
        lst = []
    
    


i = 99
b = Employee()
while(i != 0):

    print("\noptions: \n 1:add employee \n 2: employees in a department \n 3:find manager of department \n 4:find employyes based on skill \n 5:total employees in every departments \n 6:total employees in all departments \nenter 0 to exit")
    i = int(input("\nenter an option:"))
    if i == 1:
        b.add_emp()
    elif i == 2:
        b.dep_emp_find()
    elif i == 3:
        b.find_manager()
    elif i == 4:
        b.find_skill()
    elif i == 5:
        b.employee_dep()
    elif i == 6:
        b.emp_dep()