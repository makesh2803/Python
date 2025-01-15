num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("positive, even")
elif num < 0 and num % 2 == 0:
    print("negative, even")
elif num > 0 and num % 2 == 1:
    print("positive, odd")
elif num < 0 and num % 2 == 1:
    print("negative, odd")
elif num == 0:
    print("zero")