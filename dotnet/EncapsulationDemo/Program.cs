// See https://aka.ms/new-console-template for more information
using EncapsulationDemo;
//Console.WriteLine("Hello, World!");


var account = new BankAccount("1234567890", "John Doe", 5000);
account.DisplayAccountInfo();

account.Deposit(1500);
account.Withdraw(2000);

// Trying to set an invalid name (this will throw an exception)
try
{
    account.AccountHolder = "";
}
catch (Exception ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}

// Trying to withdraw an amount greater than balance
account.Withdraw(10000);

account.DisplayAccountInfo();
