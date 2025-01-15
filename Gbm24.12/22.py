electric_bill = int(input("Enter your bill: "))
if electric_bill < 100:
    print("Free")
elif electric_bill < 300:
    print(f"{2 * (electric_bill - 100)}")
elif electric_bill > 300:
    print(f"{400 + (5 * (electric_bill - 300))} ")