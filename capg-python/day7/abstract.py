from abc import ABC,abstractmethod

class Father(ABC):
    def display (self):
        print('I am display from father')
    @abstractmethod
    def myabstractMethod(self):
        pass

class Child(Father):
    def myabstractMethod(self):
        print('hello from child implementing')
    def show(self):
        print('I am from child class')


chi = Child()

chi.display()
chi.myabstractMethod()
chi.show()