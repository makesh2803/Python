neg_num = 0
pos_num = 0
for i in range(1,6):
    num = int(input(f'{i} number: '))
    if num > 0:
        pos_num += 1
    else:
        neg_num += 1
print(f'The amount of positive numbers: {pos_num}')
print(f'The amount of negative numbers: {neg_num}') 