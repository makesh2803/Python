temp = int(input("Enter a number of temperature: "))
if temp < 0:
    print("Freezing weather")
elif temp < 10:
    print("Very cold weather")
elif temp < 20:
    print("Cold weather")
elif temp < 30:
    print("Normal")
elif temp < 40:
    print("Hot")
elif temp > 40:
    print("Very hot")