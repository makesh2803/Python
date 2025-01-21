dictionary = {"101" : {"Ady" : "Perman", "Awtory" : "A.Gowsydow", "Sany" : 8},
              "102" : {"Ady" : "Saylanan eserler", "Awtory" : "G.Ezizow", "Sany" : 12},
              "103" : {"Ady" : "Ykbal", "Awtory" : "H.Deryayew", "Sany" : 6},
              "104" : {"Ady" : "Leyli Mejnun", "Awtory" : "N.Andalyp", "Sany" : 4},
              "105" : {"Ady" : "Oylanma bayry", "Awtory" : "K.Gurbannepesow", "Sany" : 9}}

while True:
    print("*****KITAPHANA*****")
    print("1.Kitaplary gormek\n2.Kitap almak\n3.Kitap tabsyrmak\n4.Cykmak")
    option = input("Saylan(1-4): ")
    if option == '1':
        for i,j in dictionary.items():
            print(i,'-',j)

    elif option == '2':
        book_num = input("Kitap belgisi: ")
        if book_num in dictionary:
            book_amount = int(input("Kitap sany: "))
            if book_amount <= dictionary[book_num]['Sany']:
                print(f"Siz {dictionary[book_num]["Awtory"]}-yn {dictionary[book_num]["Ady"]} kitabyndan {book_amount} sany satyn aldynyz!")
                dictionary[book_num]["Sany"] -= book_amount
            else:
                print(f"Bizde jemi {dictionary[book_num]["Sany"]} kitap bar")    
        else:
            print(f"Bizde {book_num} belgide kitap yok")
    
    elif option == '3':
        book_num = input("Kitap belgisi: ")
        if book_num in dictionary:
            book_amount = int(input("Kitap sany: "))
            print(f"Siz {dictionary[book_num]["Awtory"]}-yn {dictionary[book_num]["Ady"]} kitabyndan {book_amount} sany tabsyrdynyz!")
            dictionary[book_num]["Sany"] += book_amount
        else:
            print(f"Bizde {book_num} belgide kitap yok")

    elif option == '4':
        print("Sag bolun, Kitaphana gelip durun!")
        break

    else:
        print("Nadogry buyruk!")