while True:
    print('\nDo you want to add information? (yes/no)')
    choice = input().strip().lower()
    if choice == 'yes':
        name = input('Enter your name: ')
        age = input("Enter your age: ")
        phone = input('Enter your phone number: ')
        print('\nInformation added!')
    elif choice == 'no':
        break
    else:
        print("Please enter a valid response (yes or no).")