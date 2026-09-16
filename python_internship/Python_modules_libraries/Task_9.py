print("\n--- Write a program to calculate the difference between two dates.---")
import datetime

birth_year = int(input("Enter your birth year: "))

current_year = datetime.datetime.now()

year = current_year.year


age = year - birth_year
print(f"Your age is {age}")