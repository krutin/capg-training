# convert the prices in USD & Euro using appropriate function


# PricesList_inr =[3000,56000,45000,2300]
# def usd(lst):
#     ans = []
#     for i in lst:
#         x = i * 0.0116
#         ans.append(x)
#     return ans
# def eur(lst):
#     ans = []
#     for i in lst:
#         x = i * 0.0112
#         ans.append(x)
#     return ans
# pusd = usd(PricesList_inr)
# peur = eur(PricesList_inr)
# print(pusd)
# print(peur)
#____________________________________________________________________________________________________________
    # List the name which has more than 6 characters as lone_names list using appropriate function

# student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]

# long_names = list(filter(lambda x : len(x) > 6,student_name_list))

# print(long_names)

#____________________________________________________________________________________________________________
  #  Display the Product in ascending order based on the price of the product

# products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]

# sproducts = sorted(products, key = lambda v : v["price"])

# print(sproducts)

#____________________________________________________________________________________________________________


#You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order

# lst = [1,2,3,4,5,6,7,8]

# de = sorted(map(lambda x : x * 2,(filter(lambda x : x % 2 == 0,lst))))

# print(de)

#____________________________________________________________________________________________________________

#You have a list of cities with their population data. Sort the cities in descending order of their population.
# cities = [
#     {"name": "New York", "population": 8419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]

# scities = sorted(cities, key = lambda x : x["population"])
# scities.reverse()

# print(scities)

#____________________________________________________________________________________________________________

#You have a list of user records with email and a verification status. Extract the emails of verified users.
# users = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]

# vemails = list(filter(lambda x : x['verified'] == True,users))

# emails = [user['email'] for user in vemails]
# print(emails)
#____________________________________________________________________________________________________________
#You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and return the updated prices.
#list out discounted products

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
#    ]

# dproducts = list(map(lambda x : x * 0.80,filter(lambda x : x['price']> 100,products)))
# for product in products:
#     if(product['price'] > 100):
#         product['price'] = round(product['price'] * 0.80)
# print("dproducts: ",dproducts)

#____________________________________________________________________________________________________________
#Sort them in ascending order of their lengths.
# words = ["apple", "banana", "cherry", "date", "fig"]
# swords = sorted(words,key = len)
# print(swords)
#____________________________________________________________________________________________________________
#write a program to remove the duplicates in the list
# numbers3=[2,2,4,6,3,4,6,1]
# num = list(set(numbers3))
# print(num)
#____________________________________________________________________________________________________________

#count the item frequency from the below products and store it in dictionary
# products = "yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
# lst = products.split(" ")
# print(lst)
# dct = {}
# for p in lst:
#     if p not in dct:
#         dct[p] = 1
#     else:
#         dct[p] += 1
# print(dct)

#____________________________________________________________________________________________________________
#calculate the current stock and display current stock

# initial_stock = {"apple": 50,"banana": 100,"orange": 75}
# sold_item = {"apple": 10, "banana": 20, "orange": 15}
# remaining_stock = {}
# for p in initial_stock:
#     remaining_stock[p] = initial_stock[p] - sold_item[p]
# print(remaining_stock)
#____________________________________________________________________________________________________________

#You have sales data for different regions and want to calculate the total sales for each region.

# sales_data = [
#     {"region": "North", "sales": 15000},
#     {"region": "South", "sales": 8000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
# ]

# total_sales = {}

# for p in sales_data:
#     if p['region'] not in total_sales:
#         total_sales[p['region']]  = 0
#     total_sales[p['region']] += p['sales']

# print(total_sales)
#____________________________________________________________________________________________________________
#take input of your mobile number and display it in word format

# dct = {
#     "1": 'one',
#     '2':'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '0': 'zero',
# }

# number = (input("Enter your 10 digit mobile number: "))
# word = ""
# for number in number:
#     word += dct[number]
#     word += " "

# print(word)

#____________________________________________________________________________________________________________

   
