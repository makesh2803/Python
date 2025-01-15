side1 = int(input("Enter a side of triangle: "))
side2 = int(input("Enter a side of triangle: "))
side3 = int(input("Enter a side of triangle: "))
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")