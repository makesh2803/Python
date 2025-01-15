name = input('Enter your name: ')
letters = 0
for letter in name:
    if letter.isalpha():
        letters += 1
print("The amount:", letters)
# print(len(name))