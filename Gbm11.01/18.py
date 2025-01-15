import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        break
print('Congratulations👏')
print(f'This round took you {guesses} guesses')

if guesses <= 5:
    print(f'You did well. You\'re lucky')
else:
    print(f"Better luck next time")
