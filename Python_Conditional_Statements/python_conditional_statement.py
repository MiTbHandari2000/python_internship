print("\n--- Program 1 Check if person is eligible for vote  ---")

user_Age = int(input("Enter your Age: "))

if user_Age >= 18:
    print("You're Eligible for Voting")
else:
    print("You're not Eligible for voting")

print("\n--- Program 2 Grade calculator based on Marks  ---")

user_Marks = int(input("Enter your marks here: "))

if user_Marks >= 90:
    print("Your Grade is A")
elif user_Marks >= 80:
    print("Your Grade is B")
else:
    print("Your Grade is C")

print("\n--- Program 3 Traffic Light Simulator  ---")

user_Response = input("Enter the color of Traffic light: ")

if user_Response == "red":
    print("------STOP------")
elif user_Response == "yellow":
    print("-------Wait-------")
elif user_Response == "green":
    print("-----GO------")
else:
    print("Enter A Valid Input")

print("\n--- Program 4 ATM Withdrawal Check  ---")

total_Balance = 1000
withdrawal_Balance = int(input("Enter the Withdrawal Amount: "))


if withdrawal_Balance <= total_Balance:
    print("Please Collect your Cash")
    remaining_Balance = total_Balance - withdrawal_Balance
    print(f"Your Remaining balance is {remaining_Balance}")
else:
    print("You don't Have Sufficient Balance")

print("\n--- Program 5 Check number is +,-,0  ---")

number = int(input("Enter the number you want to check: "))

if number == 0 :
    print("Number is Zero")
elif number > 0 :
    print("Number is Positive")
else:
    print("Number is Negative")

print("\n--- Program 6 Check if Numbe lies in the Range  ---")

num = int(input("Enter the Number: "))

if (num > 50 and num < 100):
    print("Number is in Range")
else:
    print("Number is not in Range")

print("\n--- Program 7 UserName & Password Verification  ---")

name = "Mit123"
default_password = "Mit@123"

user_Name = input("Enter the User Name: ")
password = input("Enter the Password: ")

if user_Name == name and default_password == password :
    print("UserName & Password verified ")
else:
    print("Enter proper UserName and Password")

print("\n--- Program 8 Electricity Calculator  ---")

unit_Rate = 8

unit_Consumed = int(input("Enter the Number of Units Consumed: "))

final_Bill_Amount = unit_Rate * unit_Consumed

print(f"YOUR TOTAL BILL IS {final_Bill_Amount} ")

print("\n--- Program 9 Simple Calculator  ---")

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

sum_of_Number = num1 + num2
subst_of_Number = num1 - num2
multiplication_of_number = num1 * num2
division_of_Number = num1 / num2

print(f"sum of numbers is: {sum_of_Number} subtraction of numbers is: {subst_of_Number} multiplication of number is: {multiplication_of_number} division of Number is: {division_of_Number} ")

print("\n--- Program 10 Check the type of Triangle: Equilateral,isosceles,Scalene  ---")

length_1 = int(input("Enter the First side length Of TRiangle: "))
length_2 = int(input("Enter the Second side length Of TRiangle: "))
length_3 = int(input("Enter the Third side length Of TRiangle: "))


if length_1 == length_2 == length_3:
    print("The Type of Triangle is Equilateral")
elif length_1 == length_2 or length_1 == length_3 or length_2 == length_3:
    print("The Type of Triangle is Isosceles")
else:
    print("The Type of Triangle is Scalene")