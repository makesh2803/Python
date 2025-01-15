sum = 0
num = int(input('How many numbers input: '))
for i in range(1,num + 1):
    n = int(input(f'{i} number: '))
    sum += n
print('Sum: ', sum)