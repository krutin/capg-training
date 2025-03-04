def seperator(lst):
    even = []
    odd = []
    for ele in lst:
        if(ele%2!=0):
            odd.append(ele)
        else:
            even.append(ele)
    print("even:" , even)
    print("odd:" , odd)


n = int(input("Enter number of elements in the list:"))
lst = []
for _ in range(n):
    x = int(input("Enter the number:"))
    lst.append(x)

seperator(lst)
