using System;

class BankAccount
{
    private decimal balance; 

    public BankAccount(decimal initialBalance)
    {
        if (initialBalance >= 0)
            balance = initialBalance;
        else
            throw new ArgumentException("Initial balance cannot be negative.");
    }

    public decimal GetBalance()
    {
        return balance; 
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
            Console.WriteLine($"Deposited: {amount:C}. New Balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public bool Withdraw(decimal amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            Console.WriteLine($"Withdrawn: {amount:C}. Remaining Balance: {balance:C}");
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
//             BankAccount myAccount = new BankAccount(500);
//             Console.WriteLine($"Initial Balance: {myAccount.GetBalance():C}");
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