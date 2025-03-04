using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class OOPsDemo
    {
        string name = "";
        public OOPsDemo()
        {
            Console.WriteLine("Constructor Called");
        }
        public OOPsDemo(string company)
        {
            Console.WriteLine("Constructor Called with Company Name: " + company);
        }
        public OOPsDemo(OOPsDemo obj)
        {
            Console.WriteLine("Copy Constructor");
            Console.WriteLine(obj.name);
        }
    }
}