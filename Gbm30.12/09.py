# even_n = 0
# odd_n = 0
# while True:
#     n = int(input('Enter any number: '))
#     if n == 0:
#         break
#     elif not n % 2 == 0:    # elif n % 2 != 0: 
#         odd_n += 1
#     elif n % 2 == 0:
#         even_n += 1
# print('Number of even numbers: ', even_n)
# print('Number of odd numbers: ', odd_n)


even_n = 0
odd_n = 0
numbers = (1,2,3,4,5,6,7,8,9,10)
for n in numbers:
    if not n % 2 == 0:    # elif n % 2 != 0: 
        odd_n += 1
    elif n % 2 == 0:
        even_n += 1
print('Number of even numbers: ', even_n)
print('Number of odd numbers: ', odd_n)


