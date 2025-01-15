telefon_belgi = {'Anna':'63188199',
'Gurban':'63115599',
'Oraz':'62111444'}
person = input('Kimin telefon belgisi gerek? ')
if person in telefon_belgi:
    print(f"{person} - yn telefon belgisi {telefon_belgi[person]}")
else:
    print(f"{person} - yn telefon belgisi tapylmady")