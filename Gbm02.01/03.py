num_a = int(input('Enter A: '))
num_b = int(input('Enter A: '))
sum_of_squares = 0
for num in range(num_a, num_b + 1):
    num **= 2
    sum_of_squares += num
print("Sum of squares: ",sum_of_squares)
    # print(num)