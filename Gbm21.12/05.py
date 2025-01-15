print("""
<<< Menu >>>
1. Tea
2. Coffee
3. Water
4. Fruit juice
""")
drink = int(input("What would you like to drink? "))
if drink == 1:
    print("You chose Tea")
elif drink == 2:
    print("You chose Coffee")
elif drink == 3:
    print("You chose Water")
elif drink == 4:
    print("You chose Fruit juice")
else:
    print("I didn't understand")
