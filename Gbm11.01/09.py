numbers = []
n = 1
while True:
    num = int(input(f'Enter a {n} number in list: '))
    n += 1
    if num == 0:
        break
    else:
        numbers.append(num)
digit = int(input('Enter a number that you want to count: '))
count = 0
for num in numbers:
    if num == digit:
        count += 1
print(numbers)
print(f'{digit}-lik {count} sany bar')
