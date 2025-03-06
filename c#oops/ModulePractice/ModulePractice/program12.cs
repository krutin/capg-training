namespace ModulePractice;

public class Manager
{
    public string Name{get;set;}

    public Manager(string name)
    {
        Name = name;
    }
}

public class Department
{
    public string Name{get;set;}
    public Manager Manager{get;set;}

    public Department(string name, Manager manager)
    {
        Name = name;
        Manager = manager;
    }

    public Department ShallowCopy()
    {
        return (Department)this.MemberwiseClone();
    }

    public Department DeepCopy()
    {
        return new Department(Name, new Manager(Manager.Name));
    }
    public void Display()
    {
        Console.WriteLine($"Department: {Name}, Manager: {Manager.Name}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         // Original Object
//         Manager manager1 = new Manager("Alice");
//         Department dept1 = new Department("HR", manager1);
//
//         // Shallow Copy
//         Department shallowCopy = dept1.ShallowCopy();
//
//         // Deep Copy
//         Department deepCopy = dept1.DeepCopy();
//
//         // Modify the Manager's Name
//         dept1.Manager.Name = "Bob";
//
//         Console.WriteLine("After modifying the Manager's name:");
//         Console.WriteLine("Original: ");
//         dept1.Display();
//         Console.WriteLine("Shallow Copy: ");
//         shallowCopy.Display();
//         Console.WriteLine("Deep Copy: ");
//         deepCopy.Display();
//     }
// }