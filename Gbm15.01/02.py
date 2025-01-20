print()
dictionary = {
    'alma': '8',
    'uzum': '12',
    'hurma': '18',
    'banan': '25',
    'nar': '15'
}
summa = []
# harytlar = []
for i,j in dictionary.items():
    print(i,'-',j)
while True:
    print()
    haryt = input('Name almak isleyarsiniz? ')
    if haryt in dictionary:
        massa = int(input('Nace kg almak isleyarsiniz? '))
        x = int(dictionary[haryt]) * massa
        summa.append(x)
        # harytlar.append(haryt)
    elif haryt.lower() == 'quit':
        break
    elif haryt not in dictionary:
        print(f"{haryt.capitalize()} bizde yok")
print('Siz',float(sum(summa)),'manat tolemeli')
# print(harytlar)
