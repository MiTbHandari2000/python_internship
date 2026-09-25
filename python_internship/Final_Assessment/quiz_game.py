print("----------------------------- Quiz-game ---------------------------")

questions = [
    {
        "question": "Which symbol is used to comment a line in Python?",
        "options": "1) %  2) #  3) *",
        "answer": "2"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": "1) func  2) def  3) function",
        "answer": "2"
    },
    {
        "question": "What is a correct way to declare a Python variable??",
        "options": "1) var x = 5  2) x = 5  3) #x = 5",
        "answer": "2"
    }
]
score = 0

for q in questions:
    print(q["question"])
    print(q["options"])
    choice = input("Enter your answer: ")

    if choice == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer.")

print(f"Your final score is {score} out of {len(questions)}")