numbers = []
n = 1
while True:
    num = int(input(f"Enter a {n} number of a list: "))
    n += 1
    if num == 0:
        break
    else:
        numbers.append(num)
print(numbers)
print(f'Sonky iki element: {numbers[-2:]}')
