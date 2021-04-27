def ask_user(sentence = "Saisir un chiffre"):
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à additionner ou saisir '=' ")
    result = sum(list_numbers)
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
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
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        elif list_number!=0:
            result = result / list_number
        else:
            print('Tu divises par 0 toi ?!')
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result


def display_interface():
    i=True
    while i :
        choice = ask_user("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4
        5. Quitter""")

        choice = int(choice)
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un ciffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multiplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = division(choice)
        elif choice==5:
          print("Aurevoir")
          break
        print(f"Le resultat est ==> {result}")



