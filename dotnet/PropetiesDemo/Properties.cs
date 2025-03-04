using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PropetiesDemo
{
	internal class Person
	{
		private string _accountNumber = "34567";
		public string AccountNumber {
			get => _accountNumber;
			set => _accountNumber = value;
		}
	}
}

