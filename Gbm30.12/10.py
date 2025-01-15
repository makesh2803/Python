sum_pos = 0
sum_neg = 0
for i in range(1,6):
    num = int(input(f'{i} number: '))
    if num > 0:
        sum_pos += num
    else:
        sum_neg += num
print(f'Sum of pos number: {sum_pos} ')   
print(f'Sum of neg number: {sum_neg}')