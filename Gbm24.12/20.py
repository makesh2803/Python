num1 = int(input("Enter a number: ")) 
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num2 < num1 < num3:
    print(f"Second largest number is {num1}")
elif num1 < num2 < num3:
    print(f"Second largest number is {num2}")
elif num1 < num3 < num2:
    print(f"Second largest number is {num3}")
    