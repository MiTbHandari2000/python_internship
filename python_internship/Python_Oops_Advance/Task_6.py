print("\n--- Create a Bank system with SavingsAccount and CurrentAccount classes. ---")

class BankAccount():
    def __init__(self,balance):
        self.balance = balance

    def deposite(self,d_amount):
        self.balance = d_amount + self.balance
        return self.balance
    def withdrawal(self,w_amount):
        if w_amount > self.balance:
            print("withdrawal amount is not possible check balance: ")
        else:
            self.balance = self.balance - w_amount
            return self.balance

class SavingAccount(BankAccount):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.int_rt = interest_rate

    def calculate_interest(self):
        quaterly_time = 1
        interest = (self.balance * self.int_rt * quaterly_time ) / 100
        self.balance = self.balance + interest
        return interest
        


class CurrentAccount(BankAccount):
    def __init__(self,balance,od_limit):
        super().__init__(balance)
        self.od_limit = od_limit

    def withdrawal(self,w_amount):
        new_balance = self.balance - w_amount
        if new_balance >= -self.od_limit:

            self.balance = new_balance
            return self.balance
        else:
            print("OverDraft limit Exceeded:")
            return False

acc1 = BankAccount(0)
print(acc1.deposite(1000))
print(acc1.withdrawal(60))
saving1 = SavingAccount(169000,8.9)
print(saving1.calculate_interest())
current1 = CurrentAccount(5000,600)
print(current1.withdrawal(5700))