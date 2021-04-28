from calculate import Calculate

def display_interface():
    
    # instanciation
    tx = Calculate()
    
    # Boucle a
    a = True
    while a:
        
        choice = tx.ask_user("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4
        5. Quitter
        """)

        try:
            choice = int(choice)
            if choice == 1:
                choice = tx.ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
                result = tx.addition(choice)
            elif choice == 2:
                choice = tx.ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")
                result = tx.soustraction(choice)
            elif choice == 3:
                choice = tx.ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")
                result = tx.multplication(choice)
            elif choice == 4:
                choice = tx.ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")
                result = tx.division(choice)
            elif choice == 5:
                print("Au revoir")
                break
            print(f"Le resultat est ==> {result}")
        except:
            print("c'est pas un chiffre")
        

