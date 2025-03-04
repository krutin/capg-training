def multiplication():
    a = int(input("Enter the number for multiplication:"))
    b= int(input("enter the range for the table:"))
    for i in range(1,b+1):
        print(a ,"x", i ,"=", a*i)

multiplication()