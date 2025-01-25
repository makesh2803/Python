def print_receipt(items):
    print("\n--- Receipt ---")
    print("{:<20} {:>10} {:>10}".format("Item", "Price", "Quantity"))
    print("-" * 40)
    total = 0
    for item, details in items.items():
        price = details['price']
        quantity = details['quantity']
        total += price * quantity
        print("{:<20} {:>10.2f} {:>10}".format(item, price, quantity))
    print("-" * 40)
    print("{:<20} {:>10}".format("Total", f"${float(total)}"))
    print("-" * 40)
    print("Thank you for shopping")

def main():
    items = {}
    while True:
        print("\n--- Receipt Generator ---")
        print("1. Add item")
        print("2. View receipt")
        print("3. Finish and print receipt")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            if name in items:
                items[name]["quantity"] += quantity
            else:
                items[name] = {"price" : price, "quantity" : quantity}
            print(f"{quantity} x {name} added")
        elif choice == '2':
            if items:
                print_receipt(items)
            else:
                print("No items added yet")
        elif choice == '3':
            if items:
                print_receipt(items)
                break
            else:
                print("No items to print. Add items first")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")

if __name__ == '__main__':
    main()