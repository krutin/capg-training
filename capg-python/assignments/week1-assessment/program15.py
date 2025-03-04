

inp = 'a'

while(inp != 'q'):
    year = int(input("enter a year to check for leap year and q to quit:"))
    if(year%4 == 0):
        print("it is a leap year")
    else:
        print("it is not a leap year")