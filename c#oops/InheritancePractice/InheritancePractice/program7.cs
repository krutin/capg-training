namespace InheritancePractice;
interface IFlyable
{
    void Fly();
}

interface ISwimmable
{
    void Swim();
}

class Duck : IFlyable, ISwimmable
{
    public void Fly()
    {
        Console.WriteLine("Duck is flying.");
    }

    public void Swim()
    {
        Console.WriteLine("Duck is swimming.");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Duck myDuck = new Duck();
//         myDuck.Fly();
//         myDuck.Swim();
//     }
// }