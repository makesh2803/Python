isgarler = {"Mekan" : {"hunari":"programmist",
                       "bilimi" : "orta",        
                       "yasy" : 22},
            "Oraz" : {"hunari" : "hasapcy",
                       "bilimi" : "yokary",
                       "yasy" : 30}}
ady = input("Ady: ")
if ady in isgarler:
    isleg = input("Doly maglumat (howa/yok): ")
    if isleg == 'howa':
        print(isgarler[ady])
    else:
        mag = input("hunari/bilimi/yasy: ")
        print(isgarler[ady][mag])
else:
    print(f"{ady} atly isgar yok")