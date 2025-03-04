using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace EncapsulationDemo
{
	public class BankAccount
	{
		private readonly string _accountNumber;
		private string _accountHolder;
		private decimal _balance;

		public BankAccount(string accountNumber, string accountHolder, decimal initialBalance)
		{
			_accountNumber = accountNumber;
			_accountHolder = accountHolder;
			_balance = initialBalance > 0 ? initialBalance : throw new ArgumentException("Initial balance must be positive");
		}

		public string AccountHolder
		{
			get => _accountHolder;
			set
			{
				if (string.IsNullOrWhiteSpace(value))
					throw new ArgumentException("Account holder name cannot be empty.");
				_accountHolder = value;
			}
		}

		public string AccountNumber => _accountNumber;

		public decimal Balance => _balance;

		public void Deposit(decimal amount)
		{
			if (amount <= 0)
				throw new ArgumentException("Deposite amount must be positive");
			_balance += amount;
			Console.WriteLine($"Deposite: {amount:C}, newbalance: {_balance:C}");
		}

        public bool Withdraw(decimal amount)
        {
            if (amount <= 0)
                throw new ArgumentException("Withdrawl amount must be positive");
            if (amount > _balance)
			{
				Console.WriteLine("Insufficientbalance.");
				return false;
			}
			_balance -= amount;
            Console.WriteLine($"Withdrawn: {amount:C}, Remaining Balance: {_balance:C}");
            return true;
        }

        public void DisplayAccountInfo()
        {
            Console.WriteLine($"Account Number: {AccountNumber}, Holder: {AccountHolder}, Balance: {Balance:C}");
        }
    }
}

