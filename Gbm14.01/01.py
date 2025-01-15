import random

options = ['scissors', 'rock', 'paper']
running = True

while running:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter your choice (scissors, rock, paper): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print('It\'s a tie')
    elif player == 'scissors' and computer == 'paper':
        print('You won!')
    elif player == 'rock' and computer == 'scissors':
        print('You won!')
    elif player == 'paper' and computer == 'rock':
        print('You won!')
    else:
        print('You lost')

    if not input("Play again? (y/n): ").lower() == 'y':
        break

print("Thanks for playing!")
