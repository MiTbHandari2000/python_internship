print("\n--- Program 1: Calculate the remainder of 2 numbers ---")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
remainder = num1 % num2
print("The remainder is:", remainder)

print("\n--- Program 2: Check if number is even or odd ---")
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("\n--- Program 3: Compare two numbers and print the greater number ---")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

print("\n--- Program 4: Calculate the square and cube of a number ---")
number = int(input("Enter the number: "))
square = number ** 2
cube = number ** 3
print("The square of", number, "is", square)
print("The cube of", number, "is", cube)

print("\n--- Program 5: Check if 2 numbers are equal or not ---")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
    print("BOTH the numbers are equal")
else:
    print("The numbers are not equal")

print("\n--- Program 6: Print true if both numbers are positive, else false ---")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    print("true")
else:
    print("false")

print("\n--- Program 7: Convert float to int ---")
num = input("Enter the float number that you want to convert: ")
converted_num = int(float(num))
print(converted_num)

print("\n--- Program 8: Convert string number to int and multiply by 10 ---")
number = input("Enter the number: ")
converted_num = int(number)
result = converted_num * 10
print(result)

print("\n--- Program 9: Program that uses and & or operator for checking multiple conditions  ---")

x = True 
y = False

print(x or y)
print(x and y)

print("\n--- Program 10: divide 2 numbers and print quotient and remainder separately  ---")

x = int(input("enter the first number for division: "))
y = int(input("enter the second number for division: "))

modulo_result = x % y

quotient = x // y

print(f"the quotient for the given numbers is {quotient}, and remainder is {modulo_result}")