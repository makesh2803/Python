def user(username, password, attempt):
    limit_attempt = 0
    while limit_attempt < attempt:
        username_a = input("Enter your username: ")
        password_a = input("Enter your password: ")
        if username_a == username and password_a == password:
            print("Hos geldiniz!")
            break
        else:
            print("Username or password is incorrect")
        limit_attempt += 1

user('Gujurly', '942800', 3)