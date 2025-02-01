import random
computer_score = 0
player_score = 0
while True:
    roll = input("Do you roll a dice? (yes/no) ").lower()
    if roll == "yes":
        computer = random.randrange(1, 6)
        player = random.randrange(1, 6)
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        computer_score += computer
        player_score += player

    elif roll == "no":
        break

    else:
        print("Wrong command")

print("***** FINAL SCORE *****")
print(f"Computer: {computer_score}")
print(f"Player: {player_score}")

if player_score > computer_score:
    print("Congrulations! You won!")
elif player_score < computer_score:
    print("Congrulations! Computer won!")