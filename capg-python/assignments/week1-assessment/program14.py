def factorial(n):
    if(n < 0):
        print("Enter a positive number")
        return
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

print(factorial(4))