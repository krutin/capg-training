namespace Test_practice;

public class BankAccount
{
    private int AccountNumber { get; set; }
    private int Balance { get; set; }
    private string AccountHolderName { get; set; }

    public BankAccount(int accountnumber, int balance, string accountHolderName)
    {
        AccountNumber = accountnumber;
        if (balance < 0)
        {
            throw new ArgumentException("Balance cannot be negative");
        }
        else
        {
            Balance = balance;
        }
        AccountHolderName = accountHolderName;
    }

    public void Display()
    {
        Console.WriteLine($"Account number: {AccountNumber}, balance: {Balance}, holder name: {AccountHolderName}");
    }
    public void Deposit(int amount)
    {
        if (amount > 0)
        {
            Balance += amount;
            Console.WriteLine($"Deposited: {amount}. New Balance: {Balance}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }
    
    public bool Withdraw(int amount)
    {
        if (amount > 0 && amount <= Balance)
        {
            Balance -= amount;
            Console.WriteLine($"Withdrawn: {amount}. Remaining Balance: {Balance}");
            return true;
        }
        else
        {
            Console.WriteLine("Insufficient balance or invalid withdrawal amount.");
            return false;
        }
    }
}


// class Program
// {
//     static void Main()
//     {
//         try
//         {
//             BankAccount myAccount = new BankAccount(1234,500,"dheeraj");
//             myAccount.Display();
//
//             myAccount.Deposit(200);
//             myAccount.Withdraw(100);
//             myAccount.Withdraw(700); 
//         }
//         catch (Exception ex)
//         {
//             Console.WriteLine($"Error: {ex.Message}");
//         }
//     }
// }