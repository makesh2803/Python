# guess_count = 0
# secret_num = 9
# while guess_count < 3:
#     n = int(input('Guess the number: '))
#     if n == secret_num:
#         print('Well done!')
#         break
#     else:
#         guess_count += 1
#     print('You failed')


guess_count = 0
secret_num = 9
for i in range(3):
    n = int(input('Guess the number: '))
    if n == secret_num:
        print('Well done!')
        break
    else:
        guess_count += 1
    print('You failed')


    