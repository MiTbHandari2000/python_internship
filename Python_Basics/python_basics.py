from datetime import date

print("\n--- Program 1: Print name, age, city in a single line ---")
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Name:", name, "Age:", age, "City:", city)

print("\n--- Program 2: Sum of two numbers ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("The sum of", num1, "and", num2, "is:", total)

print("\n--- Program 3: Convert Celsius to Fahrenheit ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("\n--- Program 4: Print name in uppercase ---")
name = input("Enter your name: ")
name_upper = name.upper()
print("Your name in uppercase is:", name_upper)

print("\n--- Program 5: Calculate age from birth year ---")
birth_year = int(input("Enter your birth year: "))
current_year = date.today().year
age = current_year - birth_year
print("Your age is:", age)

print("\n--- Program 6: Swap the values of two variables ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print(a, b)

print("\n--- Program 7: Area of rectangle ---")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle is:", area)

print("\n--- Program 8: Check if number is positive, negative, or zero ---")
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\n--- Program 9: Average of two numbers ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
avg_value = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", avg_value)