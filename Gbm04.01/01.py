word = input('Input a word to reverse: ')
for letter in range(len(word) - 1, -1, -1): #range(5,-1,-1)
    print(word[letter], end='')