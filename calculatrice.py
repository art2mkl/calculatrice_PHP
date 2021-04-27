def ask_user(sentence = "Saisir un chiffre"):
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
    result = sum(list_numbers)
    return result

def multplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        else:
            result = result * list_number
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        elif list_number != 0:
                result = result / list_number
        else:
                result = 'La division par zero est impossible'
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result

def display_interface():
    a = True
    while a:
        
        choice = ask_user("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4
        5. Quitter""")


        choice = int(choice)
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")
            result = multplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")
            result = division(choice)
        elif choice == 5:
            print("Au revoir")
            break

        print(f"Le resultat est ==> {result}")
        


