#programm that print name,age,city in a single line
name = input("Enter your name: ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
print("Name:", name, "Age:", age, "City:", city)

#take two numbers from user and print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

#convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print ("Temperature in Fahrenheit:", fahrenheit)

#store your name in variable and print in uppercase
name = input("Enter your name: ")
name_upper = name.upper()
print("Your name in uppercase is:", name_upper)

#calculate age of from birth year

birth_year = int(input("Enter your birth year: "))

from datetime import date 
current_year = date.today().year
age = current_year - birth_year
print("Your age is:", age)

#swap the values of two variables
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))

a ,b = b, a
print(a,b)

#area of rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
print("Area of rectangle is:", area)

#check weather number is positive or negative
number = float(input("Enter a number: "))

if number>0:
    print("The number is positive.")
elif number<0:
    print("The number is negative.")
else:
    print("The number is zero.")

#calculate average of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

avg_value = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", avg_value)
