num_a = int(input('Enter A: '))
num_b = int(input('Enter B: '))
for i in range(num_b, num_a - 1, -1):
    print(i)
print(f'The amount: {num_b - num_a + 1}')