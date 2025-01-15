komp = input('Enter the string: ')
letters = 0
cap_letters = 0
small_letters = 0
digits = 0
spaces = 0
for letter in komp:
    if letter.isalpha():
        letters += 1
        if letter.isupper():
            cap_letters += 1
        elif letter.islower():
            small_letters += 1
    elif letter.isdigit():
        digits += 1
    else:
        spaces += 1
print(f'Letters: {letters}')
print(f'Capital letters: {cap_letters}')
print(f'Small letters: {small_letters}')
print(f'Digits: {digits}')
print(f"Spaces: {spaces}")