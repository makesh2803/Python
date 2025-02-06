import os

def change():
    for i in range(1, 11):
        old = str(i)
        new = str(i + 90)
        os.rename(old, new)
        print(f"Faylyn ady {old}-dan {new}-a owruldi")

change()