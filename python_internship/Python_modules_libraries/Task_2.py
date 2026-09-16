print("\n--- Create a module to perform string operations.---")

import stringop

str1 = input("Enter the string: ")
str2 = input ("Enter the second string: ")


print(stringop.convert_lower(str1))
print(stringop.join_string(str1,str2))
print(stringop.reverse_string(str1))
print(stringop.reverse_string(str2))
