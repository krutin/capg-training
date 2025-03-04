# class Cat:
#     def walk(self):
#         print("cat says i am hungry")

# class Horse:
#     def walk(self):
#         print("Horse says i am tierd")

# class Duck:
#     def walk(self):
#         print("duck says quackk, quackk")

# def myfunction(obj):
#     obj.walk()

# d = Duck()
# myfunction(d)

# h = Horse()
# myfunction(h)

# c = Cat()
# myfunction(c)
#____________________________________________________________________________________________________________

# class Cat:
#     def talk(self):
#         print("cat says i am hungry")

# class Horse:
#     def walk(self):
#         print("Horse says i am tierd")

# class Duck:
#     def walk(self):
#         print("duck says quackk, quackk")

# def myfunction(obj):
#     if hasattr(obj,'walk'):
#         obj.walk()
#     if hasattr(obj,'talk'):
#         obj.talk()

# d = Duck()
# myfunction(d)

# h = Horse()
# myfunction(h)

# c = Cat()
# myfunction(c)

#____________________________________________________________________________________________________________


# class Myclass:
#     def sum(self, a = None,b = None, c = None):
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = 'Provide at least Two Numbers.'
#         return s
    
# obj = Myclass()
# print(obj.sum(10,20,30))
# print(obj.sum(23,56))

# print(sum(10,20))
#____________________________________________________________________________________________________________

#method overriding

# class Add:
#     def result(self,a,b):
#         print('Addition',a+b)

# class Multi(Add):
#     def result(self, a, b):
#         super().result(a, b)
#         print('multiplication: ', a * b)

# m = Multi()
# m.result(10,20)

#____________________________________________________________________________________________________________




