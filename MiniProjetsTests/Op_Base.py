import cowsay

def calc(a, b, op):
    if op == "addition":
        return a + b
    elif op == "soustraction":
        return a - b
    elif op == "multiplication":
        return a * b
    elif op == "division":
        if b == 0:
            cowsay.cow("Erreur : Division par zéro.")
            return None  # retourne None pour indiquer une division impossible
        return a / b
    else:
        cowsay.cow("Opération non reconnue.")
        return None

# Exemple d'utilisation
try:
    print(calc(10, 0, "division"))
except ValueError as e:
    print(e)
    raise
