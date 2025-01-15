sum_pos = 0
sum_neg = 0
while True:
    num = int(input('Enter any number: '))
    if num == 0:
        break
    elif num > 0:
        sum_pos += num
    elif num < 0:
        sum_neg += num
print('Sum of all the positive numbers:', sum_pos)
print('Sum of all the negative numbers:', sum_neg)

