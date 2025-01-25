def filter_even(number):
    sanlar = []
    for num in range(1, number + 1):
        if num % 2 == 0:
            sanlar.append(num)
    print(sanlar)

filter_even(20)

          