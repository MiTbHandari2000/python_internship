print("\n--- Program 1 Function to check number is prime or not  ---")

check_num = int(input("Enter the number you want to check: "))

def is_Prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False

    return True


print(is_Prime(check_num))

print("\n--- Program 2 Function to Reverse the string  ---")

user_String = input("Enter the string you want to reverse: ")



def reverse_string(string):
    result = ""

    for char in string:
       result = char + result
    
    return result

print(reverse_string(user_String))


print("\n--- Program 3 Function to Find Factorial  ---")

num = int(input("Enter the number to find factorial: "))

def factorial_num(number):
    factorial = 1 
    while number > 0:
        factorial = factorial * number
        number = number - 1
    return factorial 

print(factorial_num(num))

print("\n--- Program 4 Function to Calculate simple interest  ---")

loan_amount = float(input("Enter the loan amount: "))
rate_of_interest = float(input("Enter the interest rate: "))
loan_tenure = float(input("Enter the loan Tenure in year: "))

def calculate_simple_interest(amount,rate,ti):
    SI = (amount*rate*ti) / 100
    return SI

print(calculate_simple_interest(amount=loan_amount,rate=rate_of_interest,ti=loan_tenure))


print("\n--- Program 5 Function to find given word is palindrome  ---")

user_string = input("Enter the word to check: ")

def palindrome_checker(user_input):

    user_input = user_input.lower()
    result = ""
    for char in user_input:
        result = char + result 
    if user_input == result:
        return True
    else:
        return False
print(palindrome_checker(user_string))


print("\n--- Program 6 Function to find vowels string ---")

user_string = input("Enter the string to check ")

def vowel_counter(user_string):
    user_string = user_string.lower()
    counter = 0 

    for char in user_string:
        if char in "aeiou":
            counter += 1
    return counter

print(vowel_counter(user_string))

print("\n--- Program 7 Merge two list ---")

list1 = ["apple","pineapple","coconut"]
list2 = ["tomato","cabage","carrot"]

def merge_List(a,b):
    result = a + b

    return result

print(merge_List(list1,list2))

print("\n--- Program 8 Find the GCD of two numbers ---")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def gcd_number(input1,input2):
    gcd = 1
    for i in range(1, min(input1,input2) + 1):
        if input1 % i == 0 and input2 % i == 0:
            gcd = i 
    return gcd 


print(gcd_number(num1,num2))


print("\n--- Program 9 Find the Area of rectangle ---")

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

def area_rectangle(len,wid):
    area = len * wid
    return area

print(area_rectangle(length,width))

print("\n--- Program 10 Find the ArmstrongNumber ---")

num = int(input("Enter the number: "))

def is_armstrong(num):
    num_str = str(num)
    total_digits = len(num_str)


    total_sum = 0 


    for digit in num_str:
        d = int(digit)

        total_sum += d ** total_digits

    if total_sum == num:
        print("Number is Armstrong")
        return True
    else:
        print("Number is not Armstrong")
        return False

print(is_armstrong(num))