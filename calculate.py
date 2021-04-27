class Calculate:

    def ask_user(self, sentence = "Saisir un chiffre"):
        choice = input(f"""{sentence}\n>""")
        return choice

    def addition(self, number):
        list_numbers = []
        while number.isdigit():
            if number.isdigit():
                list_numbers.append(int(number))
            number = self.ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")
            
            while not number.isdigit() and number != "=":
                print("c'est pas ce qu'on t'as demandé")
                number = self.ask_user("Saisir un chiffre à ADDITIONNER ou saisir '=' ")

        result = sum(list_numbers)
        return result

    def multplication(self, number):
        list_numbers = []
        while number.isdigit():
            if number.isdigit():
                list_numbers.append(int(number))
            number = self.ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")

            while not number.isdigit() and number != "=":
                print("c'est pas ce qu'on t'as demandé")
                number = self.ask_user("Saisir un chiffre à MULTIPLIER ou saisir '=' ")

        for index, list_number in enumerate(list_numbers):
            if index == 0:
                result = list_number
            else:
                result = result * list_number
        return result

    def division(self, number):
        list_numbers = []
        while number.isdigit():
            if number.isdigit():
                list_numbers.append(int(number))
            number = self.ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")

            while not number.isdigit() and number != "=":
                print("c'est pas ce qu'on t'as demandé")
                number = self.ask_user("Saisir un chiffre à DIVISER ou saisir '=' ")

        for index, list_number in enumerate(list_numbers):
            if index == 0:
                result = list_number
            elif list_number != 0:
                    result = result / list_number
            else:
                    result = 'La division par zero est impossible'
        return result

    def soustraction(self,number):
        list_numbers = []
        while number.isdigit():
            if number.isdigit():
                list_numbers.append(int(number))
            number = self.ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")

            while not number.isdigit() and number != "=":
                print("c'est pas ce qu'on t'as demandé")
                number = self.ask_user("Saisir un chiffre à SOUSTRAIRE ou saisir '=' ")

        i = 0
        for list_number in list_numbers:
            if i == 0:
                result = list_number
            else:
                result = result - list_number
            i = i + 1
        return result
