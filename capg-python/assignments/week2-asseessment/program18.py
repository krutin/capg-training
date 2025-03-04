from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        print(f"Addition: {a} + {b} = {a + b}")

    def subtract(self, a, b):
        print(f"Subtraction: {a} - {b} = {a - b}")

    def multiply(self, a, b):
        print(f"Multiplication: {a} * {b} = {a * b}")

    def divide(self, a, b):
        print(f"Division: {a} / {b} = {a / b}")

calculator = BasicCalculator()
calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)
