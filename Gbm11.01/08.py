numbers = [1,2,3,1,2,1]
digit = int(input('Enter a number that you want to count: '))
count = 0
for num in numbers:
    if num == digit:
        count += 1
print(digit,'\b-lik',count,'sany bar')