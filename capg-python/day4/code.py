# def lambdaexample():
#     add_10 = lambda x:x+10
#     print(add_10(20))

# lambdaexample()


# def lambdaExample2():
#     num1 = int(input("input first number"))
#     num2 = int(input("Enter second number"))

#     product = lambda num1,num2:num1*num2

#     print(product(num1,num2))

# lambdaExample2()


# def lambdaexample3():
#     lst = [1,2,3,4]

#     mlst = map(lambda x : x+5,lst)
#     print(list(mlst))

# lambdaexample3()


# def lembdaex4():
#     check_even = lambda x : 'even' if x % 2 ==0 else 'odd'
#     print(check_even(2))
#     print(check_even(3))

# lembdaex4()

# nums = [1, 2, 3, 4, 5]
# numbers = filter(lambda x: x > 2, nums)
# print(list(numbers))

# nums = [12,3,4,22,13]
# print(sorted(nums))
# print(nums)
# nums.sort()
# print(snums)  
# print(nums)



# nums = [1,2,3,4,5]
# print(nums[1:])
# print(nums[1:3])
# nums.append(6)
# nums.insert(6,7)
# print(nums)
# nums.pop()
# print(nums.index(5))


# lst = [1,2,3,4,5]
#unpacking
# x,y,z,a,b = lst
# print(x)
# print(a)
# print(b)
# print(y)
# print(z)

# x,*y = lst
# print(x)
# print(y)

# def fetch_orders(orders,batch_size):
#     for i in range(0,len(orders),batch_size):
#         yield orders[i:i+batch_size]
#         orders=[1,2,4,24,244]
#     for batch in fetch_orders_in_batch(orders,3):
#         print('processing batch: ',batch)

# customers={
#     "name":"rishi",
#     "email":"rishi@gmail.com",
#     "phone":"123456780",
#     "age":12,
#     "is_verified":True
# }
# print(customers['name'])
# print(customers.get('name'))

# print(customer.get('birthdate'))
# print(customer)
# customer['name']= "riya sam"