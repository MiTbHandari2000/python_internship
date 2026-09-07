print("\n--- Create Rectangle class with method to find area and perimeter ---")

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return (self.length * self.width)

    def perimeter(self):
        return 2 * (self.length + self.width) 

rec = Rectangle(20,60)
print(rec.area())
print(rec.perimeter())
