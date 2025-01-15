num_a = int(input("Enter A: "))
num_b = int(input("Enter B: "))
product = 1
for num in range(num_a, num_b + 1):
    product *= num
print("Product: ", product)