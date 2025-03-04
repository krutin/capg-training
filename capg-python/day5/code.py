# keys = ['name','age','city']
# values = ['alice','25','newyork']

# mdict = dict(zip(keys,values))
# print(mdict)

# b = (1,2,3)
# result = b * 3
# print(result)

# tuple1 = (4,4)
# print()
# print(tuple1)
# print(type(tuple1))
# print(tuple1.count(4))


# a = {10,20,'python code', 'raj',40}

# for i in a:
#     print(i)



# a = set()
# print(id(a))
# n = int(input("Enter number of elements:"))

# for i in range(n):
#     el = input("Enter elements:")
#     a.add(el)

# for i in a:
#     print(i)
# print()

# print(id(a))

# class Employee:
#     def __init__(self, name, gender, salary):
#         self.name = name
#         self.gender = gender
#         self.salary = salary

#     def __str__(self):
#         return f"Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}"



# n = int(input("Enter number of employees: "))

# emps = []


# for i in range(n):
#     print(f"\nEnter details for employee {i+1}:")
#     name = input("Enter employee name: ")
#     gender = input("Enter employee gender (male/female): ").strip().lower()
#     salary = float(input("Enter employee salary: "))

#     emp = Employee(name, gender, salary)
#     emps.append(emp)


# filter_gender = input("\nEnter gender to filter by (Male/Female): ")
# filtered_emps = [emp for emp in emps if emp.gender == filter_gender]



# if filtered_emps:
#     for emp in filtered_emps:
#         print(emp)
# else:
#     print("No employees found with the specified gender.")


# class Cars:

#     total_cars = 0

#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price

#         Cars.total_cars+=1

#     def car_info(self):
#         print(f"Car Info:{self.make} {self.model} {self.year} {self.price}")
#     def get_total_Cars(cls):
#         print(f"total cars are {cls.total_cars}")
#     def calc_depreciation(self,price,year):
#         depreciation_rate=0.15
#         depreciation_value=price*((1-depreciation_rate)**year)
#         return depreciation_value

# car1=Cars("toyota","camry",2020,35000)



# class Army:
#     def __init__(self):
#         self.name = 'krutin'
#         self.gn = self.Gun()

#     def show(self):
#         print('name:', self.name)

#     class Gun:
#         def __init__(self):
#             self.name = 'ak47'
#             self.capacity = '75 rounds'
#             self.length = '34.5 In'

#         def disp(self):
#             print("Gun Name:",self.name)
#             print("Gun capacity:",self.capacity)
#             print("Gun length:",self.length)


# a = Army()
# print(a.name)
# print()
# a.show()

# print()

# print(f'a.gn {a.gn}')

# print(f'a.gn.name {a.gn.name}')
# g = a.gn
# print(g.name)
# print(g.capacity)
# print(g.length)
# print()
# g.disp()
