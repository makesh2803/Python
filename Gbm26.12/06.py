sum = 0
attempt = 0
while 3 > attempt:
    num = int(input("Enter a number: "))
    sum += num
    attempt += 1
print(f"{sum} / {attempt} = {sum / attempt}")