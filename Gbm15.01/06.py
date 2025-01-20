dictionary = {  "Anna" : {"synag_1" : 90,
                        "synag_2" : 80,
                        "synag_3" : 70},

                "Merdan" : {"synag_1" : 95,
                        "synag_2" : 85,
                        "synag_3" : 75},

                "Oraz" : {"synag_1" : 100,
                        "synag_2" : 0,
                        "synag_3" : 50}

}
ady = input('Ady: ')
if ady in dictionary:
    synag = input("Ahli synaglar (howa/yok): ")
    if synag == 'howa':
        print(dictionary[ady])
    else:
        synaglar = input("synag_1, synag_2, synag_3: ")
        print(dictionary[ady][synaglar])