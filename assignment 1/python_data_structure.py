print("\n--- Program 1 Create tuple with 5 number  ---")

thisistuple = (1,2,3,4,5)
print(thisistuple)

print("\n--- Program 2 Access third element in tuple  ---")

print(thisistuple[3])

print("\n--- Program 3 Unpack the tuple into variables  ---")

a,b,c,d,e = thisistuple
print(a,b,c,d,e)

print("\n--- Program 4 Create a set of 5 fruits  ---")

mySet = {"apple","banana","kiwi","orange","mango"}

print("\n--- Program 5 Add a new fruit to the set  ---")

mySet.add("guava")
print(mySet)

print("\n--- Program 6 Remove an element from set  ---")

mySet.remove("guava")
print(mySet)

print("\n--- Program 7 Find a union of the set  ---")

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}


result = set1.union(set2)
print(result)

print("\n--- Program 8 Find a intersection of the set  ---")

result = set1.intersection(set2)
print(result)

print("\n--- Program 9 Check if one set is subset of another  ---")

result = set1.issubset(set2)
print(result)

print("\n--- Program 10 Convert a list with duplicate values into set to remove duplicate  ---")

list1 = ["apple","banana","orange",1,2,3,"apple","banana",2]
converted_list = set(list1)
print(converted_list)

print("\n--- Program 11 Create dictionary storing students name and marks  ---")

students = {
                    "mit":{"Math":50,"Ds":60,"English":60},
                    "harsh":{"Math":60,"Ds":80,"English":64},
                    "Yug":{"Math":67,"Ds":70,"English":64}
                }
print(students)

print("\n--- Program 12 Add new key-value pair in existing dictionary  ---")
print(students.keys())
print(students.values())

students["John"] = {"Math":80,"Ds":85,"English":64}
print(students)

print("\n--- Program 13 Delete a key-value pair from dictionary  ---")

students.pop("harsh",None)
print(students)

print("\n--- Program 14 Merge two dictionary in one  ---")

d1 = {"a":50,"b":60}
d2 = {"c":64,"d":79}

d1.update(d2)
print(d1)

print("\n--- Program 15 Check if key exists in dictionary  ---")


s1 = {"Name":"john","Age":26}

print("Name" in s1 )

print("\n--- Program 16 Count the frequency of words in string using dictionary  ---")

user_Input = input("Enter the string you want to count: ")

words = user_Input.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)

print("\n--- Program 17 Find the key with maximum values ---")

marks = {
    "Mit": 85,
    "Sara": 99,
    "John": 78,
    "Alex": 95
}


max_key = max(marks,key=marks.get)
print(max_key)

print("\n--- Program 18 Reverse key and values in dictionary ---")


original_dict = {"a":1,"b":2,"c":3,"d":4}

reversed_dict = {}

for key, value in original_dict.items():
    reversed_dict[value] = key


print(reversed_dict)

print("\n--- Program 19 Update the values for specific key ---")

students = {
                    "mit":{"Math":50,"Ds":60,"English":60},
                    "harsh":{"Math":60,"Ds":80,"English":64},
                    "Yug":{"Math":67,"Ds":70,"English":64}
            }

update_student = input("Enter the name of the student to update: ") 
update_sub = input("Enter the subject of student: ")
update_marks = int(input("Enter the marks of student to update: "))
students[update_student][update_sub] = update_marks
print(students)

print("\n--- Program 20 convert the list of tuple in dictionary ---")

list_of_tuple = [("john",65),("sara",49),("wick",40)]

result_dict = dict(list_of_tuple)

print(result_dict)