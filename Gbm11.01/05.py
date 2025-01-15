numbers = [1,2,3,4,5,6]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f'Jubut sanlar: {even}, Tak sanlar: {odd}')
        