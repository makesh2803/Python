sany = 0
soz = input("Soz girizin: ")
harplar = []
for i in range(3):
    harp = input(f'{i + 1}. harp: ')
    while len(harp) != 1:
        print('Dine 1 harp girizin!')
        harp = input(f'{i + 1}-nji harpy girizin')
    harplar.append(harp)
print(f"Girizilen soz: {soz}")
for harp in harplar:
    if harp in soz:
        print(f'{harp} bar')
        sany += 1
    else:
        print(f'{harp} yok')
print(sany,'sany harp bar')


        
