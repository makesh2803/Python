price_of_bike = int(input("Enter a price of your bike: "))
if price_of_bike > 100000:
    print(f"{price_of_bike * (1 + 0.15)}")
elif 50000 < price_of_bike <= 100000:
    print(f"{price_of_bike * (1 + 0.10)}")
elif price_of_bike <= 50000:
    print(f"{price_of_bike * (1 + 0.05)}")