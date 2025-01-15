# age = 22
# # if age >= 18:
# #     message = "Eligible"
# # else:
# #     message = "Not eligible"
# message = 'Eligible' if age >= 18 else 'Not eligible'
# print(message)

# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")


count_odd = 0
count_even = 0
for number in range(1,10):
    if number % 2 == 0:
        count_even += 1 
        print(number)
    elif number % 2 == 1:
        count_odd += 1
        print(number)
print(f"We have {count_even} even numbers")
print(f"We have {count_odd} odd numbers")