import random

# Write a Python program that conducts a simple multiple-choice quiz. 
# 1. Randomly select 3 questions from the questions list without repitition and shuffle it. 
# 2. Display each question with its options to the user.
# 3. Allow the user to input their answer (A, B, C, or D).
# 4. After all 3 questions, display the user’s score (out of 3).  

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. J.K. Rowling"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "Which element is heavier than iron?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Gold", "D. Carbon"],
        "answer": "C"
    }
]

count=0
q=random.sample(questions,k=3)
random.shuffle(q)

for i in range(3):
    print(q[i]["question"])
    print(q[i]["options"])
    choice=input("Your answer (A/B/C/D): ")
    if choice.upper()== q[i]["answer"]:
        print("Correct!\n")
        count+=1
    else:
        print("Incorrect! The correct answer was ",q[i]["answer"],".\n")

print("Your score is",count,"out of 3.")





# Sample output

'''
Question 1: What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome
Your answer (A/B/C/D): C
Correct!

Question 2: Who wrote 'Hamlet'?
A. Charles Dickens
B. William Shakespeare
C. Mark Twain
D. J.K. Rowling
Your answer (A/B/C/D): B
Correct!

Question 3: Which planet is known as the Red Planet?
A. Earth
B. Mars
C. Jupiter
D. Venus
Your answer (A/B/C/D): A
Incorrect! The correct answer was B

You scored 2 out of 3!
'''