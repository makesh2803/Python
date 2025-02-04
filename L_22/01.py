import random

dictionary = {"mekdep" : "school",
              "cagalar bagy" : "kindergarden",
              "synp otagy" : "class",
              "okuwcy" : "pupil",
              "talyp" : "student",
              "kompyuter" : "computer",
              "klawiature" : "keyboard",
              "suw" : "water",
              "kitap" : "book",
              "depder" : "notebook"
}
print("Welcome to the Turkmen to English vocabulary quiz!")
print("Translate the following words from Turkmen to English!")
print("*****************************************************")
while True:
    word = random.choice(list(dictionary.keys()))
    user_answer = input(f"What is the Turkmen translation of '{word}:'").strip().lower()

    if user_answer == dictionary[word].lower():
        print("Your answer is correct!✅")
    else:
        print(f"Your answer is incorrect. The correct translation is '{dictionary[word]}'❎")