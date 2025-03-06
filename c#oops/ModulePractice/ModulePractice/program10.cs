namespace ModulePractice;

public class User
{
    public string Username { get; set; }
    public string Role { get; set; }

    public User(string username, string role)
    {
        Username = username;
        Role = role;
    }
    public virtual void AccessControl()
    {
        Console.WriteLine("This is default AccessControl");
    }
}

public class Admin : User
{
    private List<User> usersList;
    public Admin(string username, List<User> users) : base(username, "Admin")
    {
        usersList = users;
    }

    public override void AccessControl()
    {
        Console.WriteLine($"{Username}Admin has full Access.");
    }
    public void ViewAllUsers()
    {
        Console.WriteLine("\nAll Users:");
        foreach (var user in usersList)
        {
            Console.WriteLine($"Username: {user.Username}, Role: {user.Role}");
        }
    }
    public void DeleteUser(string username)
    {
        User userToRemove = usersList.Find(user => user.Username == username);
        if (userToRemove != null && userToRemove.Role != "Admin") // Admins can't delete other admins
        {
            usersList.Remove(userToRemove);
            Console.WriteLine($"{username} has been removed.");
        }
        else
        {
            Console.WriteLine("Cannot remove this user.");
        }
    }
    
}
public class Customer : User
{
    public Customer(string username) : base(username, "Customer") {}

    public override void AccessControl()
    {
        Console.WriteLine($"{Username} (Customer) has limited access.");
    }

    public void ViewProfile()
    {
        Console.WriteLine($"Profile - Username: {Username}, Role: {Role}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         List<User> users = new List<User>
//         {
//             new Admin("Alice", new List<User>()), 
//             new Customer("Bob"),
//             new Customer("Charlie")
//         };
//
//         Admin adminUser = new Admin("Alice", users);
//         users[0] = adminUser; 
//
//         while (true)
//         {
//             Console.Write("\nEnter username: ");
//             string username = Console.ReadLine();
//             User loggedInUser = users.Find(user => user.Username == username);
//
//             if (loggedInUser == null)
//             {
//                 Console.WriteLine("User not found. Try again.");
//                 continue;
//             }
//
//             loggedInUser.AccessControl();
//
//             if (loggedInUser is Admin admin)
//             {
//                 Console.WriteLine("\n1. View All Users");
//                 Console.WriteLine("2. Delete User");
//                 Console.WriteLine("3. Logout");
//                 Console.Write("Choose an option: ");
//                 string choice = Console.ReadLine();
//
//                 switch (choice)
//                 {
//                     case "1":
//                         admin.ViewAllUsers();
//                         break;
//                     case "2":
//                         Console.Write("Enter username to delete: ");
//                         string deleteUser = Console.ReadLine();
//                         admin.DeleteUser(deleteUser);
//                         break;
//                     case "3":
//                         Console.WriteLine("Logging out...");
//                         break;
//                     default:
//                         Console.WriteLine("Invalid choice.");
//                         break;
//                 }
//             }
//             else if (loggedInUser is Customer customer)
//             {
//                 Console.WriteLine("\n1. View Profile");
//                 Console.WriteLine("2. Logout");
//                 Console.Write("Choose an option: ");
//                 string choice = Console.ReadLine();
//
//                 switch (choice)
//                 {
//                     case "1":
//                         customer.ViewProfile();
//                         break;
//                     case "2":
//                         Console.WriteLine("Logging out...");
//                         break;
//                     default:
//                         Console.WriteLine("Invalid choice.");
//                         break;
//                 }
//             }
//         }
//     }
// }