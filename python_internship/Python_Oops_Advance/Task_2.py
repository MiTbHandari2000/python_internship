print("\n--- Create  class hierarchy for Vehicle -> Car -> Electric car ---")

class Vehicle():
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self,brand,num_doors):
        super().__init__(brand)
        self.num_doors = num_doors


    
class Electric_car(Car):
    def __init__(self,brand,num_doors,battery_capacity):
        super().__init__(brand,num_doors)
        self.battery_capacity = battery_capacity

    
my_ev = Electric_car("Tesla",4,"85 KWH")
print(my_ev.brand)
print(my_ev.num_doors)
print(my_ev.battery_capacity)