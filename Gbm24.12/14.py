num = int(input("Enter number of electric unit: "))
if num <= 100:
    amount = 0
if 100 < num <= 200 :
    amount = (num - 100) * 5
if num > 200:
    amount = 500 + (num - 200) * 10
print("Amount to pay: ",amount)