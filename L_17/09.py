def factorial():
    kop = 1
    if san > 0:
        for i in range(1, san + 1):
            kop *= i
        return kop
    else:
        print("Yalnys san")

san = int(input("San girizin: "))
print("Faktoriyal: ",factorial())

