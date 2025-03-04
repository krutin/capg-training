class Car:
    def move(self):
        print("Car is driving on the road")

class Airplane:
    def move(self):
        print("Airplane is flying in the sky")

class FlyingCar(Car, Airplane):
    def move(self):
        print("FlyingCar is both driving and flying")
        Car.move(self)
        Airplane.move(self)

flying_car = FlyingCar()
flying_car.move()