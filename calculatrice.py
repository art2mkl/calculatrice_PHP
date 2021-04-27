def ask_user(sentence = "Saisir un chiffre"):
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
<<<<<<< HEAD
        number = ask_user("Saisir un chiffre à additionner ou saisir '=' ")
=======
        number = ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
    result = sum(list_numbers)
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
<<<<<<< HEAD
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
=======
        number = ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
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
<<<<<<< HEAD
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        elif list_number!=0:
            result = result / list_number
        else:
            print('Tu divises par 0 toi ?!')
=======
        number = ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        elif list_number != 0:
                result = result / list_number
        else:
                result = 'La division par zero est impossible'
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
<<<<<<< HEAD
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
=======
        number = ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result


def display_interface():
<<<<<<< HEAD
    i=True
    while i :
=======
    a = True
    while a:
        
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
        choice = ask_user("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4
        5. Quitter""")

<<<<<<< HEAD
        choice = int(choice)
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
=======

        choice = int(choice)
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")
            result = soustraction(choice)
        elif choice == 3:
<<<<<<< HEAD
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multiplication(choice)
=======
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")
            result = multplication(choice)
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")
            result = division(choice)
<<<<<<< HEAD
        elif choice==5:
          print("Aurevoir")
          break
        print(f"Le resultat est ==> {result}")

=======
        elif choice == 5:
            print("Au revoir")
            break

        print(f"Le resultat est ==> {result}")
        
>>>>>>> 1c212b2921fdde3e4d5cc6b93c0e38dc6e72423d


