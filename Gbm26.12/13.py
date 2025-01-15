phone = input("Enter your phone number: ")
total_paid = 0
while True:
    payment = input("Please pay: ")
    if payment == "quit":
        break
    else:
        total_paid += int(payment)
    print(f"You paid {total_paid} manats")
print(f"{total_paid} manats were transferred to {phone}")


