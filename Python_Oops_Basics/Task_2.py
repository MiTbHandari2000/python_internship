print("\n--- Create BankAccount class with the methods Deposite and withdraw ---")

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def deposite(self,d_amount):
        self.balance = d_amount + self.balance
        return self.balance
    def withdraw(self,w_amount):
        self.balance = self.balance - w_amount
        return self.balance

my_account = BankAccount(1000)
my_account.deposite(500)
print(my_account.balance)
my_account.withdraw(1000)
print(my_account.balance)

