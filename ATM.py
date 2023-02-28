class atm:
    def  balance(self):
       balance=0
        
       self.balance=0
       print("create an account",self.balance)
    def  deposit(self):
        amt=int(input("enter the amount:"))
        self.balance=self.balance+amt
        print("new balance:",self.balance)
    def withdraw(self):
        amt=int(input("enterv withdraw amount:"))
        if self.balance<amt:
                print("insuffient amount entered:")
        else :
                self.balance=self.balance-amt
                print("remaining balance:",self.balance)
    def enquiry(self):
        print("balance is :",self.balance)

a=atm()
a.balance()
a.deposit()
a.withdraw()
a.enquiry()
