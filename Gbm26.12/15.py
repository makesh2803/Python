# name = input("Enter your name: ")
# while name == "":
#     print("you didn't enter your name")
#     name = input("Enter your name: ")
# print("Hello",name,"how are you")



# age = int(input("Enter your age: "))
# while age < 0:
#     print('Age can\'t be negative')
#     age = int(input("Enter your age: "))
# print("you are", age, 'years old')

# food = input('Enter a food you like (q to quit): ')
# while not food == 'q':
#     print(f"you like {food}")
#     food = input('Enter a food you like (q to quit): ')
# print('bye')


num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f'Your number is {num}')
