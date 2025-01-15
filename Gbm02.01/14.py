numbers = []
for i in range(3):
    while True:
        try:
            num = int(input(f'{i + 1}-nji sany girizin: '))
            numbers.append(num)
            break
        except ValueError:
            print("Bu dogry san dal! Yene bir gezek synanysyn ")
numbers.sort()
# numbers.reverse()
print("Sanlaryn kiciden ulalyan tertibi: ")
print(numbers)