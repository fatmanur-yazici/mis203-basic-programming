import random
import time

print("WELCOME TO THE QUIZ GAME!")
print("Answer 5 questions and test your knowledge!")
print("------------------------------")

questions = [
    ["What is the capital of France?", "paris"],
    ["How many days are in a week?", "7"],
    ["Which planet is known as the Red Planet?", "mars"],
    ["What is 5 * 6?", "30"],
    ["Which language are we learning?", "python"]
]

random.shuffle(questions)

score = 0

for question in questions:
    print("\nGet ready!")
    time.sleep(1)

    print(question[0])
    answer = input("Your answer: ").strip().lower()

    if answer == question[1]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print("Correct answer:", question[1])

print("\nGAME OVER!")
print("Your score:", score, "/ 5")

if score == 5:
    print("Amazing! Perfect score!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
