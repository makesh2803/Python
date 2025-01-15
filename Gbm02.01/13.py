x_sany = 0
for num in range(1,101):
    if num % 7 == 0 and not num % 11 == 0:
        print(num,end=' ')
        x_sany += 1
print('\n',x_sany, 'sany san bar')