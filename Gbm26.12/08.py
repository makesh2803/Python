while True:
    print("""
    1. (**)
    2. (%)
    3. (//)
    4. (** 0.5)
    5. Exit
    """)
    amal = int(input("Haysy amal: "))
    if amal == 1:
        san = int(input("Girizjek sanyn: "))
        dereje = int(input("Girizjek derejan: "))
        print(f"{san} ** {dereje} = {san ** dereje}")
    elif amal == 2:
        san1 = int(input("Girizjek sanyn: "))
        san2 = int(input("Girizjek sanyn: "))
        print(f"{san1} % {san2} = {san1 % san2}")
    elif amal == 3:
        san1 = int(input("Girizjek sanyn: "))
        san2 = int(input("Girizjek sanyn: "))
        print(f"{san1} // {san2} = {san1 // san2}")
    elif amal == 4:
        san = int(input("Girizjek sanyn: "))
        print(san,'-yn koki', san ** 2)
    elif amal == 5:
        print('Exit')
        break
    else:
        print('I didn\'t understand')




