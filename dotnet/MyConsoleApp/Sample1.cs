using System;


namespace DemoApp1
{
    internal class Employee
    {
        int empId;
        string name, designation, location;
        double salary;

        public void GetEmployeeInfo()
        {
            Console.WriteLine("Enter the Employee Id, Name, Designation, Location, and Salary:");
            empId = Convert.ToInt32(Console.ReadLine());
            name = Console.ReadLine();
            designation = Console.ReadLine();
            location = Console.ReadLine();
            salary = Convert.ToDouble(Console.ReadLine());
        }

        public void PrintEmployeeInfo()
        {
            Console.WriteLine($"Employee ID: {empId} \nName: {name} \nDesignation: {designation} \nLocation: {location} \nSalary: {salary}");
        }
    }
}
