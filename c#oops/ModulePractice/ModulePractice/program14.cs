namespace ModulePractice;

sealed class SecuritySystem
{
    public void AuthenticateUser(string username, string password)
    {
        Console.WriteLine($"Authenticating {username}...");
        Console.WriteLine("Access Granted!");
    }
}



// class AdvancedSecurity : SecuritySystem
// {
//     // This will not compile because SecuritySystem is sealed
// }


// class Program
// {
//     static void Main()
//     {
//         SecuritySystem security = new SecuritySystem();
//         security.AuthenticateUser("admin", "secure123");
//     }
// }