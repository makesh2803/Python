def gosmak():
    print(f"Netije: {float(san1 + san2)}")

def ayyrmak():
    print(f"Netije: {float(san1 - san2)}")


def kopeltmek():
    print(f"Netije: {float(san1 * san2)}")


def bolmek():
    print(f"Netije: {float(san1 / san2)}")

def cykys():
    print("Sagbolun")

while True:
    san1 = float(input("Birinji sany girizin: "))
    san2 = float(input("Ikinji sany girizin: "))
    funksiya = input("Funksiya saylan: +, -, *, /\nFunksiya: ")
    if funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        if san2 != 0:
            bolmek() 
        else:
            print("San nola bolunenok")
    elif funksiya == 'quit':
        cykys()   
        break 