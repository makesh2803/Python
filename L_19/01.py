menu = {"Coffee" : {"Categorie" : "drinks", "Price" : 3},
        "Tea" : {"Categorie" : "drinks", "Price" : 2},
        "Sandwich" : {"Categorie" : "food", "Price" : 5},
        "Cake" : {"Categorie" : "desserts", "Price" : 4}   
        }
bought_products = {}
total_amount = 0
while True:
    print("Menu:")
    for i, j in menu.items():
        print(f"{i} ({j["Categorie"]}): {j["Price"]} $")
    item = input("Enter the item you want to order or 'done': ").capitalize()
    if item in menu:
        quantity = int(input("Enter the quantity: "))
        print(f"{quantity} {item}(s) added to your order")
        if item in bought_products:
            bought_products[item]["Quantity"] += quantity
        else:
            bought_products[item] = {"Quantity" : quantity, "Price" : menu[item]["Price"]}
    elif item == 'Done':
        break
    else:
        print(f"We don't have {item} in our Menu!")

for i, j in bought_products.items():
    total = j["Quantity"] * j["Price"]
    total_amount += total
    print(i, 'x', quantity, ':', total, '$')
print("Total amount:",total_amount, '$')
print("Thank you for your order!")