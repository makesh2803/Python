harytlar = { "Alma" : {"Bahasy" : 10, "Mukdary" : 20},
            "Armyt" : {"Bahasy" : 15, "Mukdary" : 10},
            "Banan" : {"Bahasy" : 25, "Mukdary" : 15},
            "Nar" : {"Bahasy" : 18, "Mukdary" : 13},
            "Hurma" : {"Bahasy" : 16, "Mukdary" : 17},
            "Mandarin" : {"Bahasy" : 23, "Mukdary" : 9},
}

kassa = 0

def haryt_gorkezmek():
    for i, j in harytlar.items():
        print(i, "- Bahasy: ", j['Bahasy'], "man,", "Mukdary: ", j['Mukdary'], "kg")

def haryt_satyn_almak():
    haryt = input("Haysy harydy satyn almak isleyaniz: ").capitalize()
    if haryt in harytlar:
        mukdar = int(input("Nace mukdarda satyn almak isleyaniz: "))
        if mukdar <= harytlar[haryt]["Mukdary"]:
            harytlar[haryt]["Mukdary"] -= mukdar
            jemi = harytlar[haryt]['Bahasy'] * mukdar
            kassa += jemi
        else:
            print(f"{haryt}-dan {mukdar}-a yeterlik mukdarda bizde yok")
    else:
        print(f"{haryt} bizde yok")

def taze_haryt_gosmak():
    haryt = input("Haysy harydy taze gosmak isleyaniz: ").capitalize()
    if haryt not in harytlar:
        bahasy = int(input("Taze harydyn bahasy: "))
        mukdary = int(input("Taze harydyn mukdary: "))
        harytlar[haryt] = {'Bahasy' : bahasy, 'Mukdary' : mukdary}
    else:
        print(f"{haryt} bizde onem bar")

def bahasyny_uytgetmek():
    haryt = input("Bahasyny uytgetjek harydyn ady: ").capitalize()
    if haryt in harytlar:
        bahasy = int(input("Harydyn taze bahasy: "))
        harytlar[haryt]["Bahasy"] = bahasy
    else:
        print(f"{haryt} bizde yok")


def harydy_ayyrmak():
    haryt = input("Ayyrjak harydyn: ").capitalize()
    if haryt in harytlar:
        harytlar.pop(haryt)
    else:
        print(f"Bizde bar bolan harydy giriz")

def mukdary_artdyrmak():
    haryt = input("Mukdaryny artdyrjak harydyny giriz: ").capitalize()
    if haryt in harytlar:
        bahasy = int(input("Harydyn mukdaryny giriz: "))
        harytlar[haryt]["Mukdary"] = bahasy
    else:
        print(f"Bizde bar bolan harydy giriz")
    
def cek():
    print(f"Kassa: {sum(kassa)}")

def cykys():
    print("Gelip durun")

while True:
    print("*** DUKAN DOLANDYRYSY ***")
    print("1. Haryt gorkezijilerini gor")
    print("2. Haryt satyn al")
    print("3. Harytlary gos")
    print("4. Harytlaryn bahasyny uytget")
    print("5. Harytlary ayyr")
    print("6. Mukdary artdyr")
    print("7. Kassany gor")
    print("Cykys ucin 'quit' yazyn")
    operation = input('Nama etmeli (san girizin): ')
    if operation == "1":
        haryt_gorkezmek()

    elif operation == "2":
        haryt_satyn_almak()

    elif operation == "3":
        taze_haryt_gosmak()

    elif operation == "4":
        bahasyny_uytgetmek()
    
    elif operation == "5":
        harydy_ayyrmak()

    elif operation == "6":
        mukdary_artdyrmak()

    elif operation == "7":
        cek()

    elif operation == "quit":
        cykys()
        break