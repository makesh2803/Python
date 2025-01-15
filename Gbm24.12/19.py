age = int(input("Enter your age: "))
gender = input("M(male) or F(female): ").upper()
days = int(input("How many days did your work: "))
if 18 <= age < 30 and gender == 'M':
    print(f"Salary: {days * 700}")
elif 18 <= age < 30 and gender == 'F':
    print(f"Salary: {days * 750}")
elif 30 <= age <= 40  and gender == 'M':
    print(f"Salary: {days * 800}")
elif 30 <= age <= 40  and gender == 'F':
    print(f"Salary: {days * 850}")
else:
    print("I didn't understand")






