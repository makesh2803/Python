def number():
    numbers = []
    while True:
        num = int(input("Enter any number: "))
        if num == 0:
            break
        else:
            numbers.append(num)
    print(f"In uly san: {max(numbers)}, In kici san: {min(numbers)}")

number()