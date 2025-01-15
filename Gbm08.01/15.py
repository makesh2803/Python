soz = input('Enter the string: ').lower()
harp = input('Letter: ').lower()
sana = 0
for i in soz:
    if i == harp:
        sana += 1
print('The amount:',sana)