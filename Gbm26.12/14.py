print("The price of 0.5 Pepsi is 5 manats")
price = 5
total_paid = 0
while total_paid < price:
    payment = int(input("Please pay: "))
    if total_paid == price:
        break
    else:
        total_paid += payment
    print(f"You paid {total_paid} manats!")
print("Take a 0.5 pepsi")
