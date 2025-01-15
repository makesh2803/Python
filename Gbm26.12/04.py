# num = int(input("Enter any number: "))
# reverse = 0
# reverse_num = 0
# while num != 0:
#     reverse = num % 10
#     reverse_num = reverse_num * 10 + reverse
#     num = num // 10
# print(f"Reverse number is {reverse_num}")

num = int(input("Enter a number:\t"))
if num < 0:
    print("Factorial isn't defined.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    print(f"The factorial of {num} is {factorial}")