# for i in range(5):
    # print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(1,6):
#     print('Software')

# for i in range(1,6):
#     print(i,'Software')

# for i in range(1,6):
#     print('Software')
#     print('Best group')

# for i in range(1,6):
#     print('Software')
# print('Best group')

# for i in range(10,51,10):
#     print(i)

# for i in range(10,1,-2):
#     print(i)

# price = int(input('Enter price of 1 kg of sweets: '))
# for i in range(1,11):
#     print('Cost of',i,'kg sweet is',price * i,'manats!')

# for i in range(1,6):
#     a = int(input(f"{i}-number: "))

# n = int(input('How many numbers input: '))
# for i in range(1,n + 1):
#     a = int(input(f"{i}-number: "))

n = int(input('How many subjects do you learn? '))
jem = 0
for i in range(1,n + 1):
    grade = int(input(f"{i}-subject's grade: "))
    jem += grade
print('Average:',jem // n)