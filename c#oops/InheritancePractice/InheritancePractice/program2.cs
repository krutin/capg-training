namespace InheritancePractice;


class Vehicle1
{
    public string Brand { get; set; }
    public int Speed { get; set; }

    public Vehicle1(string brand, int speed)
    {
        Brand = brand;
        Speed = speed;
    }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed} km/h");
    }
}

class Car1 : Vehicle1
{
    public int NumberOfDoors { get; set; }

    public Car1(string brand, int speed, int numberOfDoors) : base(brand, speed)
    {
        NumberOfDoors = numberOfDoors;
    }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Doors: {NumberOfDoors}");
    }
}

class Bike1 : Vehicle1
{
    public bool HasGear { get; set; }

    public Bike1(string brand, int speed, bool hasGear) : base(brand, speed)
    {
        HasGear = hasGear;
    }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Has Gear: {HasGear}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Vehicle1 myCar = new Car1("Toyota", 180, 4);
//         myCar.DisplayInfo();
//
//         Console.WriteLine();
//
//         Vehicle1 myBike = new Bike1("Yamaha", 120, true);
//         myBike.DisplayInfo();
//     }
// }