def is_prime(num):
    if num < 2:
        print("Not prime number.")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

st = int(input("enter start number:"))
en = int(input("Enter end number:"))

ans = []
for num in range(st, en + 1):
    if is_prime(num):
        ans.append(num)
print(ans)
