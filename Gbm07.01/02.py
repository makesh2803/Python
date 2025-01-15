# def greet_user(name):
#     # name = 'John'
#     print(f'Hi {name}')
#     print('Welcome aboard')
# print('Start')
# greet_user('John')
# print('Finish')

## 🤔 We don't repeat 2 times names:➡
def greet_user(first_name, last_name): ### name is parameter
    # name = 'John'
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print('Start')
greet_user('John', 'Smith') ### John is an argument
greet_user('Mary', 'Adams') ### Mary is an argument
print('Finish')
