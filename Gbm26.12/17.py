num = int(input("How many: "))
while num >= 1:
    if num % 2 == 0:
        print(num, num * '5')
    else:
        print(num, num * '7')
    num -= 1
