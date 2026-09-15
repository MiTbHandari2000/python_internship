print("\n--- Create a polymorphic function that works with different shapes. ---")
import math
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius*self.radius) 

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)
class Triangle():
    def __init__(self,base,height):
        self.base = base 
        self.height = height
    def area(self):
        return (self.base * self.height) / 2

def print_area(shape):
    print(shape.area())

circle1 = Circle(4)
rect1 = Rectangle(20,30)
triangle1 = Triangle(14,32)

print_area(circle1)
print_area(rect1)
print_area(triangle1)