numbers = [1,2,3,2,4,1]
sanlar = []
for num in numbers:
    if num not in sanlar:
        sanlar.append(num)
print(sanlar)