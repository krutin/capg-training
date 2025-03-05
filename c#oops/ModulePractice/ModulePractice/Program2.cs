using System;

class Student
{
    private string name;
    private int rollNo;

    public string Name
    {
        get { return name; }
        set
        {
            if (!string.IsNullOrWhiteSpace(value))
                name = value;
            else
                throw new ArgumentException("Name cannot be empty or whitespace.");
        }
    }

    public int RollNo
    {
        get { return rollNo; }
        set
        {
            if (value > 0)
                rollNo = value;
            else
                throw new ArgumentException("Roll Number cannot be negative or zero.");
        }
    }

    public Student(string name, int rollNo)
    {
        Name = name; 
        RollNo = rollNo;
    }

    public void Display()
    {
        Console.WriteLine($"Student Name: {Name}, Roll No: {RollNo}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         try
//         {
//             Student student1 = new Student("Alice", 101);
//             student1.Display();
//
//             Student student2 = new Student("", -5);  
//             student2.Display();
//         }
//         catch (Exception ex)
//         {
//             Console.WriteLine($"Error: {ex.Message}");
//         }
//     }
// }