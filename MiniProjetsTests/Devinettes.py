import random

def jeu_deviner_nombre():
    nombre_secret = random.randint(1, 10)
    print("Devinez le nombre entre 1 et 10.")
    while True:
        try:
            choix = int(input("Votre choix: "))
            if choix == nombre_secret:
                print("Bravo ! Vous avez deviné.")
                break
            else:
                print("Mauvais choix, essayez encore.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

jeu_deviner_nombre()
