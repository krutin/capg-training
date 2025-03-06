namespace ModulePractice;

using System;

interface IVehicle
{
    void Drive();
}

class Car1 : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Driving a Car...");
    }
}

class Bike : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Riding a Bike...");
    }
}

class VehicleFactory
{
    public static IVehicle GetVehicle(string vehicleType)
    {
        return vehicleType.ToLower() switch
        {
            "car" => new Car1(),
            "bike" => new Bike(),
            _ => throw new ArgumentException("Invalid vehicle type")
        };
    }
}

// class Program
// {
//     static void Main()
//     {
//         IVehicle vehicle1 = VehicleFactory.GetVehicle("car");
//         vehicle1.Drive();
//
//         IVehicle vehicle2 = VehicleFactory.GetVehicle("bike");
//         vehicle2.Drive();
//     }
// }