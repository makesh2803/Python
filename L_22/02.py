import random
print("Men bir san sayladym. Siz ony tapyp bilersinizmi?")
while True:
    min_num = int(input("In kici san saylan: "))
    max_num = int(input("In uly san saylan: "))
    if min_num > max_num:
        print("Min number max number-den uly bolup bilmeyar")
    else:
        break
    
chosen_number = random.randint(min_num, max_num)
chance = 0

while chance < 5:
    guess = int(input("Sany caklan: "))
    chance += 1
    if guess == chosen_number:
        print(f"Dogry tapdynyz! Siz {chance} synanysykda tapmagy basardynyz")
        break
    elif chance == 5:
        print(f"Siz bilip bilmediniz. Bellenen san {chosen_number}")
        break
    elif chosen_number > guess:
        print("Sizin caklamanyz kici.")
    elif chosen_number < guess:
        print("Sizin caklamanyz uly.")
    


