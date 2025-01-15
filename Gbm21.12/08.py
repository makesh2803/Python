num = int(input("Enter a number: "))
if num < 10 and num % 2 == 0:
    print("one digit, even")
elif num < 10 and num % 2 == 1:
    print("one digit, odd")
elif num < 100 and num % 2 == 0:
    print("two digit, even")
elif num < 100 and num % 2 == 1:
    print("two digit, odd")
elif num < 1000 and num % 2 == 0:
    print("three digit, even")
elif num < 1000 and num % 2 == 1:
    print("three digit, odd")
else:
    print("I didn't understand")