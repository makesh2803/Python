import random
options = ["picture", "number"]
number_score = 0
picture_score = 0
for i in range(1, 11):
    number = random.choice(options)
    if number == "number":
        number_score += 1
    else:
        picture_score += 1
    print(f'{i} {number}')

print(f"NUMBER: {number_score}")
print(f"PICTURE: {picture_score}")

if number_score > picture_score:
    print("Most tossed NUMBER")
elif number_score < picture_score:
    print("Most tossed PICTURE")
    
