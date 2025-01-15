while True:
    password = input("Type your password: ")
    if len(password) >= 8:
        print("Accepted password")
        break
    else:
        print("Please type new password")

