# class Emp:
#     def __init__(self,name):
#         print("I am default init")
#     def __init__(self,name):
#         self.name = name
#         print(name)
#     def demo(self):
#         print("This is a demo method")
#         print(self.name)
# emp2 = Emp("krutin")
# emp2.demo()



# class example:
#     def __init__(self,*args):
#         if len(args) == 1:
#             print(f"hello {args[0]}")
#         elif len(args) == 2:
#             print(f"hello {args[0]}, you are {args[1]} years old.")
    

# obj1 = example("alice")
# obj1 = example("bob",10)


# class example:
#     def __init__(self,**kwargs):
#         if "name" in  kwargs and "age":
#             print(f"hello {kwargs['name']}, you are {kwargs['age']} years old.")
#         elif 'name' in kwargs:
#             print(f"hello {kwargs['name']}")
    

# obj1 = example("alice")
# obj1 = example("bob",10)


# class Grandparent:
#     def __init__(self):
#         self.grandparent_property = "Grandparent's Property"

#     def show_grandparent(self):
#         print("This is the Grandparent class.")


# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         self.parent_property = "Parent's Property"

#     def show_parent(self):
#         print("This is the Parent class.")


# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.child_property = "Child's Property"

#     def show_child(self):
#         print("This is the Child class.")


# obj = Child()
# objp = Parent()

# print(obj.grandparent_property)  
# print(obj.parent_property)       
# print(obj.child_property)        

# obj.show_grandparent()  
# obj.show_parent()       
# obj.show_child()        

# class Father:
#     def skill(self):
#         print("Father: Knows Driving")

# class Mother:
#     def hobby(self):
#         print("Mother: Loves Painting")

# class Child(Father, Mother):
#     def own_talent(self):
#         print("Child: Good at Coding")

# obj = Child()
# obj.skill()
# obj.hobby()
# obj.own_talent()





