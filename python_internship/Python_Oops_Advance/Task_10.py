print("\n--- Demonstrate the use of super() in inheritance. ---")

class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"this is car is from  {self.brand} and the price is {self.price}")

class Electric(Car):
    def __init__(self,brand,price,rangeLeft):
        super().__init__(brand,price)
        self.rangeLeft = rangeLeft
    
    def run(self):
        print(f"this car is from {self.brand} and it's price is {self.price} and it has range of {self.rangeLeft} ")

car1 = Car("Ford",50000)
car1.show_details()
car2 = Electric("Tesla",99999,500)
car2.run()