def pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

def reversepattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter number of rows in pattern"))
p = input("do you want patter in straight or reverse order press 'r' for reverse and  any other letter for straight:")
if(p == 'r'):
    reversepattern(n)
else:
    pattern(n)
