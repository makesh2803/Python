import random
name = input("What is your name? ")
print(f"Good luck! {name}")
words = ['rainbow', 'computer', 'science', 'board',
        'programming', 'python', 'mathematics', 'water',
        'player', 'condition', 'reverse', 'geeks']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        print(f"The word is {word}")
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses")
        if turns == 0:
            print("You loose")