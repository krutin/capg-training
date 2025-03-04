# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"



class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_car_info(self):
        return f"{self.display_info()}, Fuel Type: {self.fuel_type}"



class Bike(Vehicle):
    def __init__(self, brand, model, bike):
        super().__init__(brand, model)
        self.bike = bike

    def display_bike_info(self):
        return f"{self.display_info()}, Bike Type: {self.bike}"



class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, fuel_type="Electric")
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        return f"{self.display_car_info()}, Battery Capacity: {self.battery_capacity} kWh"



if __name__ == "__main__":
    vehicle = Vehicle(brand="Benz", model="G-wagon")
    print(vehicle.display_info())


    car = Car(brand="Benz", model="CLA-200", fuel_type="Petrol")
    print(car.display_car_info())


    bike = Bike(brand="Royal-Emfield", model="classic 350", bike="Cruiser")
    print(bike.display_bike_info())


    electric_car = ElectricCar(brand="Tesla", model="Model S", battery_capacity=100)
    print(electric_car.display_electric_car_info())