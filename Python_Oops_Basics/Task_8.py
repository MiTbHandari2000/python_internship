print("\n--- Create Laptop class with method to apply discount on price  ---")

class Laptop:
    def __init__(self,model,price):
        self.model = model
        self.price = price
    
    def apply_discount(self,discount_percent):
       discount_amount = (self.price * discount_percent) / 100
       final_price = self.price - discount_amount
    #    self.price = final_price
       return final_price

lapt1 = Laptop("dell",1000)
print(lapt1.apply_discount(10))

