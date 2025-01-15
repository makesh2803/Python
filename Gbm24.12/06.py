print("""
1. (+)
2. (-)
3. (*)
4. (/)
""")
amal = int(input("Haysy amal: "))
san_1 = int(input("Birinji san: "))
san_2 = int(input("Ikinji san: "))
if amal == 1:
    print(f"{san_1} + {san_2} = {san_1 + san_2}")
elif amal == 2:
    print(f"{san_1} - {san_2} = {san_1 - san_2}")
elif amal == 3:
    print(f"{san_1} * {san_2} = {san_1 * san_2}")
elif amal == 4:
    print(f"{san_1} / {san_2} = {san_1 / san_2}")
else:
    print("I didn't understand")
    