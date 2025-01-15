num_of_years = int(input("How many years have you been working:\n"))
if num_of_years < 6:
    print(f"{num_of_years * (1 + 0.05)}")
elif 6 <= num_of_years <= 10:
    print(f"{num_of_years * (1 + 0.08)}")
elif num_of_years > 10:
    print(f"{num_of_years * (1 + 0.1)}")