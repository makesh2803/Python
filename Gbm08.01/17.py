name = input('Enter your name: ')
vowel = 0
consonant = 0
for letter in name:
    if letter in ('a','e','y','u','i','o'):
        vowel += 1
    elif letter in ('q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'):
        consonant += 1
    # else:
print('The amount of vowel:',vowel)
print('The amount of consonant:',consonant)



