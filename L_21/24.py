rooms = {101 : None, 102 : None, 103 : None,
         104 : None, 105 : None}
prices = {101 : 100, 102 : 120, 103 : 150,
          104 : 200, 105 : 250}
total_earnings = 0

def show_rooms():
    print("\nRoom status:")
    for room, guest in rooms.items():
        print(f"Room: {room}: {'Available' if guest is None else 'Occupied'}")

def book_room():
    show_rooms()
    room = int(input("\nEnter room to book: "))
    if room in rooms and rooms[room] is None:
        name = input("Enter guest name: ")
        rooms[room] = name
        print(f"Room {room} booked for another {name}")
    else:
        print("Room not available or invalid number")

def checkout():
    global total_earnings
    room = int(input("\nEnter room to checkout: "))
    if room in rooms and rooms[room] is not None:
        total_earnings += prices[room]
        print(f"{rooms[room]} checked out. Room {room} is now free")
        rooms[room] = None
    else:
        print("Invalid room number or already vacant")
    
def show_earnings():
    print(f"\nTotal Earnings: $ {total_earnings}")

while True:
    print("\n1. Show rooms\n2. Book\n3. Checkout\n4. Show Earnings\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        show_rooms()
    elif choice == '2':
        book_room()
    elif choice == '3':
        checkout()
    elif choice == '4':
        show_earnings()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again")
        