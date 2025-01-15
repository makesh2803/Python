a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = (b ** 2) - (4 * a * c)
print("Diskriminant:",d)
if d > 0:
    print(f"x1 = {(-b + (d ** 0.5)) / ( * a) }")
    print(f"x2 = {(-b - (d ** 0.5)) / (2 * a) }")
if d == 0:
    print(f"x1 = {- b / (2 * a)}")
if d < 0:
    print("No roots")
