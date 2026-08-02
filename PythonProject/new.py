questions =("Whats 5+5?: ",
            "What is the product of 4 * 7?: ",
            "How many colors are in the rainbow?: ",
            "What is my favorite show?: ",
            "What is the last number before 100?: ")

options = (("A. 10","B. 33", "C. Fire"),
           ("A. 36","B. One piece", "C. 28"),
           ("A. 12","B. 22", "C. 8"),
           ("A.Dragon Ball Z ","B. Adventure Time", "C. Breaking Bad"),
           ("A. 100","B. 99", "C. infinite amount"),)

answers = ("A", "C", "C", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------")
    print(question)
    for option in options [question_num]:
        print(option)
    guess = input("Enter (A,B,C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("Correct!")
    else:
        print("Wrong..!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
print("------------")
print("   Results  ")
print("------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
