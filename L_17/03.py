def factorial(number):
    multiple = 1
    for num in range(1, number + 1):
        multiple *= num
    print(f"Factorial of {number} is {multiple}")
factorial(4)