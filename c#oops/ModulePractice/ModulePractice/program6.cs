namespace ModulePractice;

public class Person
{
    public string Name { get; set; }
    public string Role { get; set; }
    public Person(string name, string role)
    {
        Name = name;
        Role = role;
    }
    public virtual void GetDetails()
    {
        Console.WriteLine("name: " + Name + ", role: " + Role);
    }
}

public class Teacher : Person
{
    private int Salary{ get; set; }

    public Teacher(string name, string role, int salary) : base(name, role)
    {
        Salary = salary;
    }

    public override void GetDetails()
    {
        Console.WriteLine($"Student: {Name}, Age: {Role}, Course: {Salary}");
    }
}

public class Student : Person
{
    private string Class { get; set; }

    public Student(string name, string role, string standard) : base(name, role)
    {
        Class = standard;
    }
    public override void GetDetails()
    {
        Console.WriteLine($"Student: {Name}, Age: {Role}, Course: {Class}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Person p1 = new Person("shankar", "Engineer");
//         Person p2 = new Teacher("sai", "teacher", 2000);
//         Person p3 = new Student("krutin", "student", "6th");
//         p1.GetDetails();
//         p2.GetDetails();
//         p3.GetDetails();
//     }
// }