namespace ModulePractice;

public class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle default start");
    }
}

public class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car default start");
    }
}

public class bike : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("bike default start");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Vehicle v1 = new Vehicle();
//         v1.Start();
//         Vehicle c1 = new Car();
//         c1.Start();
//         Vehicle b1 = new bike();
//         b1.Start();
//     }
// }