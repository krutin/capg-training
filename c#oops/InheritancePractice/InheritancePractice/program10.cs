namespace InheritancePractice;

using System;

sealed class SecuritySystem
{
    public void AuthenticateUser()
    {
        Console.WriteLine("User authenticated successfully.");
    }
}


// class AdvancedSecuritySystem : SecuritySystem
// {
// }

class Program
{
    static void Main()
    {
        SecuritySystem system = new SecuritySystem();
        system.AuthenticateUser();
    }
}