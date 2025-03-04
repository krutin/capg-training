# class my_account:
#     def __init__(self):
#         self.ammount = 0
#     def check_balance(self):
#         print(self.ammount)
#     def deposite(self,a):
#         self.ammount += a
#         print("balance after deposite is:",{self.ammount})
#     def withdrawl(self,a):
#         if(self.ammount>=a):
#             self.ammount -= a
#             print("Successfully withdrawn" ,a, "rupees ,balance after withdrawl is: ",{self.ammount})
#         else:
#             print("insufficient funds for withdrawl")

# krutin_account = my_account()

# krutin_account.check_balance()
# krutin_account.deposite(500)
# krutin_account.withdrawl(1000)
# krutin_account.withdrawl(100)
#_______________________________________________________________________________________________
        
# def temp_conv():
#     temp = int(input("Enter temperature to convert:-"))
#     conv = input("Enter type of temperatue \n 'c' for celsius \n 'f' for farenheit \n 'k' for kelvin:")

#     if(conv=="c"):
#         print("temperature in farenheit is:", (temp*5/9)+32)
#         print("temperature in kelvin is :", temp + 273.5)
#     elif(conv == "f"):
#         print("temp in celsius is:", (temp - 32) * 5/9)
#         print("temp in kelvin is:", ((temp - 32) * 5/9) + 273.5)
#     elif(conv == "f"):
#         print("temp in celsius is:", temp - 273.15)
#         print("temp in faranheit is:", ((temp - 273.5) * 9/5) + 32)
#     else:
#         print("input a correct format for type of temperature")
#         temp_conv()
# temp_conv()



#_______________________________________________________________________________________________


# import random

# def game():
#     ans = random.randint(1,101)
#     while(True):
#         number = int(input("Guess the number"))
#         if(number>ans):
#             print("Too high")
#         elif(number<ans):
#             print("Too low")
#         else:
#             print("YOU WON")
#             break

# game()

#_______________________________________________________________________________________________


# def grading():
#     name = input("enter students name:")
#     print("Enter marks acoording to subject asked out of 100")
#     eng = int(input("Enter marks for english:"))
#     san = int(input("Enter marks for sanshrith:"))
#     mat = int(input("Enter marks for Math:"))
#     phy = int(input("Enter marks for physics:"))
#     che = int(input("Enter marks for chemestry:"))

#     total = eng+san+mat+phy+che
#     per = total/5
#     if(per>=85):
#         grade = 'A'
#         print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
#     elif(per>=75 and per<85):
#         grade = 'B'
#         print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
#     elif(per>=65 and per<75):
#         grade = 'C'
#         print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
#     elif(per>=55 and per<65):
#         grade = 'D'        
#         print("Student name:",name,"\nTotal:", total, "\nPercentage:",per,"\nGrade:",grade)
#     elif(per<55):
#         print("Try again next semester, student",name,"failed")
    
# grading()

#_______________________________________________________________________________________________

# class shopping():
#     def __init__(self):
#         print("welcome to xyz shop what would you like to shop today")
#         self.cart = {}
#     def add_item(self,item,price):
#         self.cart[item] = price
#     def view_cart(self):
#         items = list(self.cart.keys())
#         print("The items in cart are:\n", items)
#     def items_price(self):
#         price = sum(self.cart.values())
#         print("The price of items in cart is:\n", price)

# bag = shopping()
# bag.add_item("pen",20)
# bag.add_item("pencil",20)
# bag.add_item("phone",20)
# bag.add_item("watch",20)
# bag.items_price()
# bag.view_cart()

#_______________________________________________________________________________________________

# def is_prime(num):
#     if num < 2:
#         print("Not prime number.")
#         return

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# st = int(input("enter start number:"))
# en = int(input("Enter end number:"))

# ans = []
# for num in range(st, en + 1):
#     if is_prime(num):
#         ans.append(num)
# print(ans)

#_______________________________________________________________________________________________


# def check_loan(salary,age,credit_score):
#     if(age < 18 or credit_score < 600):
#         return "not approved. credit score low"
#     elif(salary < 50000):
#         return "not approved. salary too low"
#     else:
#         return "Loan Approved!"

# salary = int(input("enter salary:"))
# age = int(input("enter age:"))
# credit_score = int(input("Enter credit score:"))

# print(check_loan(salary, age, credit_score))

#_______________________________________________________________________________________________


# def multiplication():
#     a = int(input("Enter the number for multiplication:"))
#     b= int(input("enter the range for the table:"))
#     for i in range(1,b+1):
#         print(a ,"x", i ,"=", a*i)

# multiplication()

#_______________________________________________________________________________________________

# def string_analyse():
#     s = input("Enter a string you want to analyse:\n")
#     vowels, cons , num , special = 0,0,0,0
#     for cha in s:
#         if(cha.lower() in ["a","e","i","o","u"]):
#             vowels += 1
#         elif(cha.isalpha()):
#             cons += 1
#         elif(cha.isnumeric()):
#             num += 1
#         else:
#             special += 1
#     print("The string contains\n {} vowels, {} consonants, {} numbers and {} special charectors".format(vowels,cons,num,special))


# string_analyse()

#_______________________________________________________________________________________________


# def bill_splitter():
#     bill = int(input("enter bill amount:"))
#     members = int(input("enter the number of members to split the bill:"))
#     tip = int(input("enter tip percentage of tip to add"))

#     tip_amount = (tip / 100 ) * bill

#     total = bill + tip_amount
#     split = total/members
#     print("The amount each person should pay is: ", split)

# bill_splitter()


#_______________________________________________________________________________________________


# def password_checker():
#     s = input("Enter a password to check")

#     if(len(s)<8):
#         return "password too short, try again"

#     u = l = d = spe = False
#     for char in s:
#         if(char.isupper()):
#             u  = True
#         elif(char.islower()):
#             l = True
#         elif(char.isnumeric()):
#             d = True
#         else:
#             spe = True
#     if(not u):
#         return "password must contain lower letters, try again"
#     if(not l):
#         return "password must contain upper letters, try again"
#     if(not d):
#         return "password must contain numbers, try again"
#     if(not spe):
#         return "password must contain special characters, try again"
    
#     return "strong password."
# print(password_checker())

#_______________________________________________________________________________________________


# def pattern(n):
#     for i in range(1, n + 1):
#         print("*" * i)

# def reversepattern(n):
#     for i in range(n, 0, -1):
#         print("*" * i)

# n = int(input("Enter number of rows in pattern"))
# p = input("do you want patter in straight or reverse order press 'r' for reverse and  any other letter for straight:")
# if(p == 'r'):
#     reversepattern(n)
# else:
#     pattern(n)


#_______________________________________________________________________________________________

# def pal(st):
#     return st == st[::-1]


# inp = ''
# while(inp != 'q'):
#     inp = input("enter a string to check palindrome and q to quit: ")
#     print(pal(inp))


#_______________________________________________________________________________________________


# def factorial(n):
#     if(n < 0):
#         print("Enter a positive number")
#         return
#     ans = 1
#     for i in range(1,n+1):
#         ans *= i
#     return ans

# print(factorial(4))
#_______________________________________________________________________________________________


# inp = 'a'

# while(inp != 'q'):
#     year = int(input("enter a year to check for leap year and q to quit:"))
#     if(year%4 == 0):
#         print("it is a leap year")
#     else:
#         print("it is not a leap year")


#_______________________________________________________________________________________________


# def seperator(lst):
#     even = []
#     odd = []
#     for ele in lst:
#         if(ele%2!=0):
#             odd.append(ele)
#         else:
#             even.append(ele)
#     print("even:" , even)
#     print("odd:" , odd)


# n = int(input("Enter number of elements in the list:"))
# lst = []
# for _ in range(n):
#     x = int(input("Enter the number:"))
#     lst.append(x)

# seperator(lst)

#_______________________________________________________________________________________________


# def calc_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         category = "underweight"
#     elif 18.5 <= bmi < 24.9:
#         category = "normal"
#     elif 25 <= bmi < 29.9:
#         category = "overweight"
#     else:
#         category = "obese"
#     return bmi, category

# weight = float(input("Enter weight in kg:"))
# height = float(input("Enter height in meters:"))
# bmi, category = calc_bmi(weight, height)
# print("BMI: {}, Category: {}".format(bmi, category))

#_______________________________________________________________________________________________



