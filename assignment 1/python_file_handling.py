print("\n--- Program 1 Programm to read file and display its contents  ---")

with open("sample.txt","r") as file:
    content = file.read()
print(content)


print("\n--- Program 2 Programm to count the line in File  ---")

with open("sample.txt","r") as f:
    content = f.readlines()
    count = len(content)

print(f"Total number of lines: {count}")


print("\n--- Program 3 Programm to count each word appears in file  ---")

with open("sample.txt","r") as f:
    file_content = f.read()
   
    result = file_content.split()
    word_freq = {}
    for word in result:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    

print(word_freq)


print("\n--- Program 4 Enter 5 user-entered sentence to the file  ---")



with open("newfile.txt","w+") as f:
    print("Enter 5 sentences:")

    for i in range(1,6):
        sentence = input(f"Sentence{i}: ")
        f.write(sentence + "\n") 

    f.seek(0)
    show_sentences= f.read()
    print(show_sentences)    
print("Successfully saved 5 sentences to newfile.txt")


print("\n--- Program 5 Write a programm to append a list of string to existing file  ---")

my_list = ["apple","banana","cheryy"]
with open("sample.txt","a+") as f:
        for item in my_list:
            f.write(item + "\n")
        
        f.seek(0)
        content=f.read()
        print(content)

print("\n--- Program 6 Write a programm to read file and print only lines containing specific words  ---")

user_input = input("Enter the specific-word you want to check: ")

with open("sample.txt","r") as file:

    content_of_file = file.readlines()
    for line in content_of_file:
        if user_input in line:
            print(line,end="")


print("\n--- Program 7 Write a programm to replace specific word in file and save changes  ---")

targeted_word = input("Enter the word to find: ")
replaceable_word  = input("Enter the word you want to replace it with: ")

with open("newfile.txt","r") as f:
    content = f.read()
    new_content = content.replace(targeted_word,replaceable_word)

with open("newfile.txt","w") as file:
    file.write(new_content)

print("\n--- Program 8 Write a programm to merge content of two file to third file  ---")

with open("sample.txt","r") as file1:
    content1 = file1.read()

with open("newfile.txt","r") as file2:
    content2 = file2.read()

final_content = content1 + "\n" + content2

with open("combined_file.txt","w") as final:
    final.write(final_content)

print("\n--- Program 9 Write a programm to read csv file and print its content in formatted way ---")

import csv

with open("waaree.csv","r") as f:
    reader = csv.reader(f)
    header = next(reader)
    
    print(f"{'Symbol':<15}{'Date':<15}{'Delivery Qty':<15}")
    
    for row in reader:
        print(f"{row[0]:<15}{row[2]:<15}{row[13]:<15}")
        

print("\n--- Program 10 Write a programm to backup a file by copying its content to another file ---")



with open("sample.txt","r") as f:
    content = f.read()

with open("backup.txt","w") as newF:
    newF.write(content)