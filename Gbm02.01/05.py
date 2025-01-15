num_a = int(input("Enter A: "))
num_b = int(input("Enter B: "))
if num_a < num_b:
    for num in range(num_a, num_b + 1):
        print(num)
else:
    for num in range(num_b, num_a + 1):
        print(num)

