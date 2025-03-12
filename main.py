# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Adam Krejčí
# email: adam.krejci.1915@gmail.com

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "lizz": "pass123"
}

TEXTS = {
    "1": '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    "2": '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    "3": '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if users.get(username) == password:
        print(f"username:{username}")
        print(f"password:{password}")
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        print("We have 3 texts to be analyzed.")
        print("----------------------------------------")
        text_number = input("Enter a number between 1 and 3 to select a text: ")
        
        if text_number in TEXTS:
            selected_text = TEXTS[text_number]
            word_count = len(selected_text.split())
            titlecase_count = sum(1 for word in selected_text.split() if word.istitle())
            uppercase_count = sum(1 for word in selected_text.split() if word.isupper())
            lowercase_count = sum(1 for word in selected_text.split() if word.islower())
            numericstring_count = sum(1 for word in selected_text.split() if word.isnumeric())
            numbers_text = [int(word) for word in selected_text.split() if word.isdigit()]
            total_sum = sum(numbers_text)
           
            import string
            word_lengths = {}
            clean_text = selected_text.translate(str.maketrans("", "", string.punctuation))
            for word in clean_text.split():
                length = len(word)
                if length in word_lengths:
                    word_lengths[length] += 1
                else:
                     word_lengths[length] = 1

            print(f"Enter a number btw. 1 and 3 to select: {text_number}")
            print("----------------------------------------")
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numericstring_count} numeric strings.")
            print(f"The sum of all the numbers {total_sum}.")
            print("----------------------------------------")
            print(f"{"LEN":<3}|{"OCCURENCES":<20}|{"NR":<5}")
            print("----------------------------------------")
            for length, count in sorted(word_lengths.items()):
                stars = "*" * count
                print(f"{length:<3}|{stars:<20}|{count:<5}")
                
        else:
            print(f"Enter a number btw. 1 and 3 to select: {text_number}")
            print("wrong input, terminating the program..")

    else:
        print(f"username:{username}")
        print(f"password:{password}")
        print("unregistred user, terminating the program..")

login()