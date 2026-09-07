print("\n--- Program 1 take string input and print its length  ---")

user_input = input("enter the string ")
print(len(user_input))

print("\n--- Program 2 convert sentence to lowercase  ---")

txt = input("enter the string you want to convert ")
converted_txt = txt.lower()
print("converted text is : ",converted_txt)


print("\n--- Program 3 replace space with underscore in the string  ---")

txt = "Hello World In Python"
result = txt.replace(" ","_")
print(result)

print("\n--- Program 4 Extract the first and last character of the string  ---")

txt = 'hello world'
print(txt[0])
print(txt[-1])

print("\n--- Program 5 Reverse the string using slicing   ---")

a = 'Hello World'
print(a[::-1])

print("\n--- Program 6 Count how many times letter appears in string   ---")

a = input("enter the string: ")
txt = input("enter the character you want to check: ")

result = a.count(txt)
print(result)

print("\n--- Program 7 Check if word is present in sentence   ---")

user_Input = input("enter the sentence: ")
check_word = input("enter which word to check: ")

print(check_word in user_Input)

print("\n--- Program 8 Take a name,age and print using f-string   ---")

user_Name = input("enter your name: ")
user_Age = int(input("enter your age: "))

print(f"Your name is: {user_Name} and Your age is : {user_Age}" )

print("\n--- Program 9 Remove extra space from start and end of the strings  ---")

a = " hello world "
print(a.strip())

print("\n--- Program 10 Join the ListofWords into a single string  ---")

words = ["Hello","to","the","world","of","python"]
result = "-".join(words)
print(result)

print("\n--- Program 11 Create list of 5 fav movies  ---")

fav_Movie = ["MIB","LOP","Avengers","Spider-man","iron-man"]
print(fav_Movie)

print("\n--- Program 12 Add new movie to the list  ---")

result = fav_Movie.append(input("enter your one fav Movie: "))
print(fav_Movie)

print("\n--- Program 13 Remove the first movie from the list  ---")

print(fav_Movie.pop(0))

print("\n--- Program 14 Sort list of number in Ascending order  ---")

numeric_List = [1,4,5,6,7,3,2]
numeric_List.sort()

print(numeric_List)

print("\n--- Program 15 Reverse the List  ---")

numeric_List.sort(reverse=True)
print(numeric_List)

print("\n--- Program 16 Largest Number IN List  ---")

largest = max(numeric_List)
print(largest)

print("\n--- Program 17 Merge 2 list in 1  ---")

list1 = ["apple","banana","pineapple"]
list2 = ["tomato","coriender","chilly"]

merged_List = list1 + list2
print(merged_List)

print("\n--- Program 18 Access last element without index  ---")

my_List = ["apple","banana","blueberry","stawberry","oranges"]

last_element = next(reversed(my_List))

print(last_element)

print("\n--- Program 19 Create nested list and access specific element  ---")

nested_List = [[1,2,4,5],["tomato","onion","garlic"],["milk","butetr","cheese"]]

print(nested_List[1][2])

print("\n--- Program 20 Count the appearance of element in list  ---")

my_list = [1,2,3,4,5,6,5,6,2]
element = int(input("Enter the the element you want to count: "))

count = my_list.count(element)
print(f"{element} appears {count} times in the list.")