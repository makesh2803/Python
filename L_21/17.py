import random
print("*** ARITHMETIC GAME PROGRAM ***")
questions = 0
correct_answers = 0
while True:
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    solution = a + b
    isleg = input("Do you want continue (yes/no): ").lower()
    if isleg == "yes":
        print(f"{a} + {b} =?")
        ans = int(input("Your answer: "))
        if ans == solution:
            print("Your answer is correct!")
            correct_answers += 1
        else:
            print(f"Your answer is incorrect! Correct answer is: {solution}")
        questions += 1
    elif isleg == "no":
        break
    else:
        print("Wrong command")

print("*****YOUR RESULT*****")
print(f"Questions: {questions}")
print(f"Correct answers: {correct_answers}")
percent = (100 * correct_answers) / questions
print(percent, "%")