print("\n--- Implement the method overidinig in the base and derived classs ---")

class Vehicle():
    def start(self):
        print("Vehicle is staring: ")

class Car(Vehicle):
    def start(self):
        print("Car Engine is Starting: ")


v = Vehicle()
v.start()
start_car = Car()
start_car.start()