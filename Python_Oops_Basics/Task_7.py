print("\n--- Create Circle class to find area & circumference ---")
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_of_circle(self):
        return math.pi * self.radius * self.radius
    def circum_of_circle(self):
        return 2*math.pi*self.radius

result = Circle(30)
print(result.area_of_circle())
print(result.circum_of_circle())
