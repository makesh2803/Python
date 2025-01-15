x = int(input("Total number of working days: ")) 
y = int(input("Total number of days for absent: "))
percent = ((x - y) / x) * 100
print(percent)
if percent < 75:
    print("Not able to continue")
elif percent < 100:
    print("You can continue")