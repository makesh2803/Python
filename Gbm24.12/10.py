# inputted_numbers = 0
sum_of_numbers = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    else:
        # inputted_numbers += 1
        sum_of_numbers += num
print(f"Sum: {sum_of_numbers}")
