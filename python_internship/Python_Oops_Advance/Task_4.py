print("\n---Demonstrate multiple inheritance with two parent classes ---")

class Flyable():

    def fly(self):
        print("Duck is flying: ")

class Swimmable():
    def swim(self):
        print("Duck is swimming in the water")


class Duck(Flyable,Swimmable):
    pass


duck_fly = Duck()
duck_fly.fly()
duck_fly.swim()