print("\n--- Create a car class with attributes like Brand model and speed and methods to accelerate/brake ---")

class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
        print(f"Car is accelerating with the speed of {self.speed} ")
    def brake(self):
        self.speed -= 30
        print(f"Car is braking with speed of {self.speed} ")

my_car = Car("Toyota", "Corolla", 50)
my_car.accelerate()
my_car.brake()