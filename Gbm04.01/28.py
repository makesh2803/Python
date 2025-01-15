phone_number = input('Enter your phone number: ')
digits_mapping = {
    '1':'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
    }
output = ''
for ch in phone_number:
    output += digits_mapping.get(ch, '!') + ' '
print(output)