num = int(input('How many: '))
i = 1
while i <= num:
    if i % 2 == 0:
        print(i, i * '@')
    else:
        print(i, i * '&')
    i += 1