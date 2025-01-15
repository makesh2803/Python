# i = 1
# num = int(input("Enter any number: "))
# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i += 1

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
if num1 > num2:
    while num1 > num2:
        if num2 % 2 == 0:
            print(num2)
        num2 += 1
else:
    while num1 < num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1