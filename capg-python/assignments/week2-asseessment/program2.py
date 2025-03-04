class my_account:
    def __init__(self):
        self.ammount = 0
    def check_balance(self):
        print(self.ammount)
    def deposite(self,a):
        self.ammount += a
        print("balance after deposite is:",{self.ammount})
    def withdrawl(self,a):
        if(self.ammount>=a):
            self.ammount -= a
            print("Successfully withdrawn" ,a, "rupees ,balance after withdrawl is: ",{self.ammount})
        else:
            print("insufficient funds for withdrawl")

krutin_account = my_account()

krutin_account.check_balance()
krutin_account.deposite(500)
krutin_account.withdrawl(1000)
krutin_account.withdrawl(100)