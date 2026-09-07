print("\n--- Create Student class with the methods to calulate Average marks ---")

class Student:
    def __init__(self,marks):
        self.marks = marks
        
    def averageMarks(self):
        return (sum(self.marks)) / len(self.marks)
student1 = Student([100,50,60,80,90])
result = student1.averageMarks()
print(result)
