words = []
while True:
    word = input("Enter a word: ")
    if word == '0':
        break
    else:
        words.append(word)
print(' '.join(words))
