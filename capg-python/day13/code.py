# def log_execution(func):
#     def wrapper():
#         print("this is custom decorator")
#         func()
#     return wrapper

# @log_execution
# def sample():
#     print("this is function")

# sample()

# #______________________________________________________________________

# def log_executioner(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         print(res)
#         return res
#     return wrapper


# @log_executioner
# def add(a,b):
#     return a + b

# add(5,6)