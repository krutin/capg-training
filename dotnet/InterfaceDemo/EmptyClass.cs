using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using System;

namespace MultipleInheritanceDemo
{
    internal class Student
    {
        public int StudentId { get; } 
        public string Domain { get; }

        
        public Student(int id, string domain)
        {
            StudentId = id;
            Domain = domain;
        }

        public virtual void DisplayStudentInfo()
        {
            Console.WriteLine($"Student ID: {StudentId}, Domain: {Domain}");
        }
    }
}

