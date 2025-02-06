import os
def main():
    number = int(input("Nace sany folder doretmekci: "))
    for i in range(1, number + 1):
        name = input("Folder ady: ")
        os.mkdir(name)

main()