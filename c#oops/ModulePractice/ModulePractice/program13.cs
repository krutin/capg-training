namespace ModulePractice;

public class Bank
{
    public string AccountHolder { get; set; }
    public int Balance { get; set; }
    public static double InterestRate { get; set; } = 5.0;

    public Bank(string accountHolder, int balance)
    {
        AccountHolder = accountHolder;
        Balance = balance;
    }
    public static void SetInterestRate(double interestRate)
    {
        InterestRate = interestRate;
    }
    public void DisplayAccountInfo()
    {
        Console.WriteLine($"Account Holder: {AccountHolder}, Balance: {Balance}, Interest Rate: {InterestRate}%");
    }
}
// class Program
// {
//     static void Main()
//     {
//         Bank acc1 = new Bank("Alice", 5000);
//         Bank acc2 = new Bank("Bob", 7000);
//
//         Console.WriteLine("Before Interest Rate Change:");
//         acc1.DisplayAccountInfo();
//         acc2.DisplayAccountInfo();
//
//         Bank.SetInterestRate(6.5);
//
//         Console.WriteLine("\nAfter Interest Rate Change:");
//         acc1.DisplayAccountInfo();
//         acc2.DisplayAccountInfo();
//     }
// }