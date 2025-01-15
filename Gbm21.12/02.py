height = int(input("Enter your height: "))
if height > 120:
    print("Can ride")
    age = int(input("What's your age: "))
    if age > 18:
        print("$12")
    elif age <= 18:
        print("$7")
else:
    print("Can't ride")