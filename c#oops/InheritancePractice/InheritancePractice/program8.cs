namespace InheritancePractice;
class Person
{
    public string Name { get; set; }

    public void ShowDetails()
    {
        Console.WriteLine($"Person: {Name}");
    }
}

class Student : Person
{
    public int StudentID { get; set; }

    public void ShowStudentID()
    {
        Console.WriteLine($"Student ID: {StudentID}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Student student = new Student { Name = "Alice", StudentID = 101 };
//
//         Person person = student; 
//         person.ShowDetails();
//
//         Student downcastedStudent = (Student)person; 
//         downcastedStudent.ShowStudentID();
//     }
// }