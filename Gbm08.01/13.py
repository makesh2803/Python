komp = input('Enter the string: ')
for letter in komp:
    if komp.count(letter) == 1:
        print(letter, '- single letter')