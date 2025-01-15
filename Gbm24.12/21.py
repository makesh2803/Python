#not working
side1 = int(input("Enter a side of triangle: "))
side2 = int(input("Enter a side of triangle: "))
side3 = int(input("Enter a side of triangle: "))
if side2 + side3 > side1 or side1 + side3 > side2 or side1 + side2 > side3:
    print("Possible")
# elif side1 + side3 > side2:
#     print("Possible")
# elif side1 + side2 > side3:
#     print("Possible")
else:
    print("not possible")

