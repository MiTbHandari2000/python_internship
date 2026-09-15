print("\n--- Create a Teacher and Student class to show inheritance. ---")

class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"Teacher is teaching {self.subject}")

class Student(Person):
    def __init__(self,name,age,grade,sub_name):
        super().__init__(name,age)
        self.grade = grade
        self.sub_name = sub_name

    def study(self):
        print(f"Student is studing {self.sub_name}")


teach1 = Teacher("vrutti",25,"Maths",60000)
stud1 = Student("Mit",26,"A","CS")
print(teach1.teach())
print(stud1.study())
print(teach1.name)
print(stud1.name)
print(stud1.age)
print(teach1.age)