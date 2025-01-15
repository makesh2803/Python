numbers = []
for i in range(3):
    valid = False
    while not valid:
        user_input = input(f'{i + 1}-nji sany girizin:')
        if all(num in '0123456789' for num in user_input) and user_input != '':
            numbers.append(int(user_input))
            valid = True
        else:
            print('Bu dogry san dal! Yene bir gezek synanysyn')
numbers.sort()
print("Sanlaryn kiciden ulalyan tertibi: ")
print(numbers)
        