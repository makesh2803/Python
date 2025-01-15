temp = int(input("Enter a temperature: "))
unit = input('C (Celcius) or F (Fahrenheit): ')
if unit == 'C':
    print(f'{temp} C is {(temp * 2) + 30} in Fahrenheit')
else:
    print(f'{temp} F is {(temp - 30) / 2} in Celcius')

# x = 'maksat'
# print(x.upper())