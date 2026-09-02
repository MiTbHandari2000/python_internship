print("\n--- Program 1and2 Programm to handle division by zero error  ---")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2 
    print(result)
except ValueError:
    print("Enter the valid Integer. ")
except ZeroDivisionError:
    print("Can't divide by zero.")

print("\n--- Program 3 Programm to handle File not Found Error & multiple exceptions   ---")

try:
    with open("xyz.csv","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File does not exists")
except PermissionError:
    print("You dont have permission to access the file")
except Exception as e:
    print("Something went wrong:",e)

print("\n--- Program 4 Programm to use finally for resource cleanup   ---")


try:
    f = open("sample.txt","r")
    content = f.read()
    result = 10 / 0
except ZeroDivisionError:
    print("Division Error occured")
finally:
    f.close()

print("\n--- Program 5 Programm to create custom exception for invalid age  ---")


user_age = int(input("Enter you age: "))
class InvalidAgeError(Exception):
    pass

def studentAge(age):
    if age < 18:
        raise InvalidAgeError("Your age is invalid ")

try:
    studentAge(user_age)
except InvalidAgeError as e:
    print("Error:",e)

print("\n--- Program 6 Programm to handle indexError while accessing the list  ---")



list1 = ["apple","banana","cherry","strawberry","pineapple"]

try:
    fruit = list1[5]
    print(fruit)
except IndexError as e:
    print("Given index is not present in the list",e)


print("\n--- Program 7 Programm that takes two numbers and handles all the possible Errors  ---")

try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    result = num1 / num2
    print(result)

except ValueError:
    print("Enter the valid integer ")
except ZeroDivisionError:
    print("Division Error occured"")
except TypeError:
    print("Error occurred.")


print("\n--- Program 8 Programm that logs Error to the file instead of printing them  ---")

import logging

logging.basicConfig(filename="error_logging.txt",level=logging.ERROR)

try:
    num = int(input("ENter the number: "))
except ValueError as e:
    logging.error(f"Invalid input: {e}")

print("\n--- Program 9 Programm that validates email format and raises and exception got invalid ones  ---")

import re

user_email = input("Enter Your Email Id: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

try:
    if not re.match(pattern,user_email):
        raise ValueError("Invalid email format")
    print("Your email is verified successfully")
except ValueError as e:
    print("Error",e)
