namespace InheritancePractice;

class Account
{
    public virtual void CalculateInterest()
    {
        Console.WriteLine("Calculating interest in Account.");
    }
}


class SavingsAccount : Account
{
    public sealed override void CalculateInterest()
    {
        Console.WriteLine("Calculating interest for Savings Account.");
    }
}


// class PremiumSavings : SavingsAccount
// {
//     public override void CalculateInterest() 
//     {
//         Console.WriteLine("Premium savings interest calculation.");
//     }
// }


// class Program
// {
//     static void Main()
//     {
//         Account acc = new Account();
//         acc.CalculateInterest(); 
//
//         SavingsAccount savings = new SavingsAccount();
//         savings.CalculateInterest();
//     }
// }