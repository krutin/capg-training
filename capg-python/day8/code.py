# # from abc import ABC,abstractmethod
# #
# # class interface1(ABC):
# #     def show():
# #         pass
# #
# # class interface2(ABC):
# #     def show():
# #         pass
# #
# # class derived(interface2,interface1):
# #     def show():
# #         print("Show methods of interface involved")
# #
# # a=derived()
# #
# # derived.show()
# #
# from abc import ABC,abstractmethod
# class Abstrackbase(ABC):
#     def __init__(self,value):
#         self.value=value
#         print("Abstract class constructor")
#
#     def show(self):
#         pass
#
# class ConcreteClass(Abstrackbase):
#     def __init__(self,value,extra):
#         super().init(value)
#         self.extra=extra
#         print("concrete class")
#     def show(self):
#         print(f"value: {self.value}, Extra: {self.extra}")
#
#
# obj=ConcreteClass(10,'Extra data')
# obj.show()

# class PublicExample:
#     def __init__(self,name):
#         self.name = name

#     def display(self):
#         print("name "+self.name)

# publicexample = PublicExample("krutin")
# print(publicexample.name)
# publicexample.display()

# class PrivateExample:
#     def __init__(self,salary):
#         self.__salary = salary #private variable
#     def __display(self): #private method
#         print("salary: ", self.__salary)

#     def access_private(self):
#         self.__display() # Allowed inside class

# obj = PrivateExample(5000)


# class ProtectedExample:
#     def __init__(self,age):
#         self._age = age
#     def _display(self):
#         print(f'Age : {self._age}')
# class SubClass(ProtectedExample):
#     def show(self):
#         print(f'Accessing protected {self._age}')
#         self._display



try:
    print("enter the net sales")

    previous = float(input("- Prior period: "))
    current = float(input("- current period: "))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'sales increase {abs(change)}%'
    else:
        result = f'sales decrease {abs(change)}%'

    print(result)

except ValueError:
    print('error! please enter a number for net')
except ZeroDivisionError:
    print('error! net sales cannot be zero')
except Exception as error:
    print(error)
