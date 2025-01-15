L = []
i = 0
while i < 5:
    num = int(input("Enter a number: "))
    L.append(num)
    i = i + 1
L.sort()
print("Largest number is:", L[-1])
print("Smallest number is:", L[0])