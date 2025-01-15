sum_num = 0
number = 0
for i in range(1,6):
    num = int(input(f"{i} number: "))
    if num > 0:
        sum_num += num
        number += 1
print(f"Average: {sum_num // number}")



