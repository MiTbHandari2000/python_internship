print("\n--- Create a custom math module and import it in another file. ---")

import mathfunc 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(mathfunc.add(num1,num2))
print(mathfunc.multiply(num1,num2))