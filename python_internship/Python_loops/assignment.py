print("\n--- 1.Print numbers from 1 to 10.---")

for i in range(1,11):
    print(i)


print("\n--- 2.Display multiplication table for a given number ---")

for i in range(1,11):
    for j in range(1,11):
        print(f" {i} * {j} = {i*j} ")



print("\n--- 3.Find factorial of a number. ---")

factorial = 1
number = int(input("Enter the number: "))
while number > 0:
    factorial = factorial * number
    number = number - 1
    
print(f"Factorial of given number is {factorial}")



print("\n--- 4.Generate the first N Fibonacci numbers. ---")

n = int(input("Enter how many fibonnaci number you want: "))
first = 0 
second = 1 

for i in range(n):
    print(first)
    first , second = second , first+ second

print("\n--- 5.Check if a number is prime. ---")

num = int(input("Enter the number to check prime: "))

def is_even(num):
    if num <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False    

    return True

print("\n--- 6.Reverse a number (e.g., 123 --> 321). ---")
num =  int(input("Enter the number to reverse: "))
reversed_num = 0

while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num // 10
    
print(reversed_num)

print("\n--- 7.Count digits in a number.---")

number = int(input("Enter the number: "))
counter = 0 
if number > 0:
    while number > 0 :
        number = number // 10
        counter += 1
else:
    counter = 1
    print("The number has 1 digit")
print(counter)

print("\n-- 8.Find sum of even numbers between 1-100. --")

sum = 0 
for i in range(1,101):
    if i % 2 == 0:
       sum += i 

print(sum)

print("\n-- 9.Print a pyramid pattern. --")

n = 4
spaces = n - 1
# print(spaces) 
star = 1

for i in range(n):
    print(" " * spaces + "*" * star )
    spaces -= 1
    star += 2

# print("\n-- Print a right align pyramid  --")

# n = 5
# spaces = n - 1


# for i in range(n):
#     print(" " * spaces + str(i)*i)
#     spaces -= 1
    
# print("\n-- Print Inverted pyramid --")
    
# n = 5
# spaces = 0
# star = n

# for i in range(n):
#     print("*" * star + " " * spaces)
#     spaces += 1
#     star -= 1
    
# print("\n-- Number triangle (not repeated digits, but counting up): --")
# n = 5


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
        
print("\n-- 10.Find all divisors of a number. --")

result = []
number = int(input("Enter the number: "))


for i in range(1,number + 1 ):
    if number % i == 0:
        result.append(i)

print(result)