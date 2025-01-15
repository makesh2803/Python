num_a = int(input('Enter A: '))
num_b = int(input('Enter B: '))
sum = 0
for num in range(num_a, num_b + 1):
    sum += num
    # print(num,end=' + ')
print('Sum:',sum)