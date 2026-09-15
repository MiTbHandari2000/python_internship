print("\n--- Create a Base class Animal and subclass Dog and Cat ---")

class Animal:

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog makes a sound")
class Cat(Animal):
    def sound(self):
        print("Cat makes a sound")
    
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()