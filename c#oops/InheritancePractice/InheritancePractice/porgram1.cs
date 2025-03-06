namespace InheritancePractice;



class Vehicle
{
    public string Brand { get; set; }
    public int Speed { get; set; }

    public Vehicle(string brand, int speed)
    {
        Brand = brand;
        Speed = speed;
    }

    public void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed} km/h");
    }
}

class Car : Vehicle
{
    public int NumberOfDoors { get; set; }

    public Car(string brand, int speed, int numberOfDoors) : base(brand, speed)
    {
        NumberOfDoors = numberOfDoors;
    }

    public void DisplayCarInfo()
    {
        DisplayInfo();
        Console.WriteLine($"Doors: {NumberOfDoors}");
    }
}

class Bike : Vehicle
{
    public bool HasGear { get; set; }

    public Bike(string brand, int speed, bool hasGear) : base(brand, speed)
    {
        HasGear = hasGear;
    }

    public void DisplayBikeInfo()
    {
        DisplayInfo();
        Console.WriteLine($"Has Gear: {HasGear}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Car car = new("Toyota", 180, 4);
//         car.DisplayCarInfo();
//
//         Bike bike = new("Yamaha", 120, true);
//         bike.DisplayBikeInfo();
//     }
// }