def custom_sort(numbers):
    if choice.upper() == 'A':
        numbers.sort()
        print(numbers)

    elif choice.upper() == 'D':
        numbers.sort(reverse = True)
        print(numbers)

choice = input("Ascending (A) or descending (D): ")
custom_sort([2,50,8,9,41])