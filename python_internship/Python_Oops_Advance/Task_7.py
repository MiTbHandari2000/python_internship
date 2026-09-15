print("\n--- Create a class with private attributes and getter/setter methods. ---")

class Bank():
    def __init__(self,balance):
        self.__balance = balance


    @property
    def get_balance(self):
        return self.__balance 

    def set_balance(self,d_amount):


        self.d_amount = d_amount

        if self.d_amount > 0:
            self.__balance += self.d_amount
        else:
            print("Enter Valid amount")
            return False

account = Bank(5000)
print(account.get_balance)
deposit = float(input("Enter the amount you want to deposit: "))
account.set_balance(deposit)
print(account.get_balance)
