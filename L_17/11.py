inventory = {}

def add_medicine(inventory):
    name = input("Enter Medicine name: ")
    price = float(input("Enter Medicine price: "))
    quantity = int(input("Enter Medicine quantity: "))
    if name in inventory:
        inventory[name]['quantity'] += quantity
        print(f"Updated {name}'s quantity to {inventory[name]['quantity']}")
    else:
        inventory[name] = {'price' : price, 'quantity' : quantity}
        print(f"Added {name} to the inventory")

def view_inventory(inventory):
    if not inventory:
        print("No medicines in the inventory")
    else:
        print("\n---Inventory---")
        for name, details in inventory.items():
            print(f"{name}:Price = $ {details['price']:.2f}, Quantity = {details['quantity']}")

def sell_medicine(inventory):
    name = input("Enter Medicine name to sell: ")
    if name in inventory:
        quantity = int(input("Enter quantity to sell" ))
        if inventory[name]['quantity'] >= quantity:
            inventory[name]['quantity'] -= 1
            total_price = inventory[name]['price'] * quantity
            print(f"Sold {quantity} units of {name} for $ {float(total_price)}")
            if inventory[name]['quantity'] == 0:
                print(f"{name} is now out of stock")
        else:
            print(f"Insufficient stock! Only {inventory[name]['quantity']} units available")
    else:
        print("Medicine not found in the inventory")

while True:
    print("\n--- Drugstore Management ---")
    print("1. Add Medicine")
    print("2. View Inventory")
    print("3. Sell Medicine")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_medicine(inventory)
    elif choice == '2':
        view_inventory(inventory)
    elif choice == '3':
        sell_medicine(inventory)
    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")
