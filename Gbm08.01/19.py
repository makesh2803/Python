name = input('Enter your name: ')
for letter in range(len(name) - 1, -1, -1):
    print(name[letter], end='')