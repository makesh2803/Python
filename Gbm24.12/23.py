days = int(input("Number of days: "))
if days <= 5:
    print(f"{days * 2}")
elif 6 <= days <= 10:
    print(f"{days * 3}")
elif 11 <= days <= 15:
    print(f"{days * 4}")
elif days > 15:
    print(f"{days * 5}")