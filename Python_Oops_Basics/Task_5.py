print("\n--- Create Employee class that displys salary details ---")

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    

    def show_details(self):
        print(f"Name: {self.name} Salary: {self.salary}")
    
emp1 = Employee("mit",70000)
emp1.show_details()