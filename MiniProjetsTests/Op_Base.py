def calc(a, b, op):
    if op == "addition":
        return a + b
    elif op == "soustraction":
        return a - b
    elif op == "multiplication":
        return a * b
    elif op == "division":
        if b == 0:
            raise ValueError("Erreur : Division par zéro.")
        return a / b
    else:
        raise ValueError("Opération non reconnue.")

# Exemple d'utilisation
try:
    print(calc(10, 0, "division"))
except ValueError as e:
    print(e)
    raise
