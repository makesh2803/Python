num = int(input('How many: '))
for i in range(1, num + 1):
    if num % 2 == 0:
        print(f"{i} {i * ' & '}")
    else:
        print(f"{i} {i * ' @ '}")
    num += 1
        