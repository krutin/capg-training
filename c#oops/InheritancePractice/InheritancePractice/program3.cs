namespace InheritancePractice;

public class Employee
{
    public string Name { get; set; }
    public int Salary { get; set; }

    public Employee(string name, int salary)
    {
        Name = name;
        Salary = salary;
        Console.WriteLine($"Employee Constructor: {Name}, Salary: {Salary}");
    }

}

public class Manager : Employee
{
    public int Bonus { get; set; }

    public Manager(string name, int salary, int bonus) : base(name, salary)
    {
        Bonus = bonus;
        Console.WriteLine($"Manager Constructor: Bonus: {Bonus}");
    }
    public void DisplayInfo()
    {
        Console.WriteLine($"Name: {Name}, Salary: {Salary}, Bonus: {Bonus}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Manager mgr = new Manager("Alice", 75000, 10000);
//         mgr.DisplayInfo();
//     }
// }