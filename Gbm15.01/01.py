dictionary = {
    'hello':'salam',
    'apple':'alma',
    'lemon':'limon',
    'cat':'pisik',
    'dog':'it',
    'flag':'baydak',
    'student':'okuwçy',
    'family':'masgala',
    'pen':'ruçka',
    'water':'suw',
    'bread':'çorek'
}
while True:
    print()
    print('***** My Dictionary Program *****\n')
    print("1. Show\n2. Add\n3. Edit\n4. Delete\n5. Exit\n")
    choice = int(input("Your choice? "))
    print()
    if choice == 1:
        for i,j in dictionary.items():
            print(i,'-',j)
    elif choice == 2:
        english_word = input('Enter the word that you want to add in English: ')
        if english_word not in dictionary:
            turkmen_word = input('Enter the word that you want to add in Turkmen: ')
            dictionary.setdefault(english_word,turkmen_word)
            print('Added successfully')
        else:
            print('The word you entered exists in dictionary. Therefore, you can\'t add it twice')
    elif choice == 3:
        edit_english = input('Enter the word that you want to edit in English: ')
        if edit_english in dictionary:
            edit_turkmen = input('Enter the word that you want to edit in Turkmen: ')
            dictionary[edit_english] = edit_turkmen
            print('Edited successfully')
        else:
            print("The word you entered doesn't exist in dictionary. Therefore, you can't edit it")
    elif choice == 4:
        delete_english = input('Enter the word that you want to delete in English: ')
        if delete_english in dictionary:
            dictionary.pop(delete_english)
            print('Deleted successfully')
        else:
            print("The word you entered doesn't exist in dictionary. Therefore, you can't delete it")
    elif choice == 5:
        print('Thanks for using program :)')
        break
    else:
        print('Wrong command...')