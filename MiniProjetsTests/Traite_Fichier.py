def lire_fichier(chemin):
    try:
        with open(chemin, 'r') as fichier:
            contenu = fichier.read()
            if not contenu:
                raise ValueError("Le fichier est vide.")
            return contenu
    except FileNotFoundError:
        raise FileNotFoundError("Fichier introuvable.")

# Exemple d'utilisation
try:
    contenu = lire_fichier("fichier_test.txt")
    print(contenu)
except Exception as e:
    print(e)
