import traceback
import lolpython
import cowsay

def main():
    try:
        # Exemple de code qui pourrait générer des erreurs
        x = 1 / 0  # Erreur intentionnelle
    except Exception as e:
        # Utiliser lolpython pour reformuler le message d'erreur
        with lolpython:
            print("Oh non, une erreur hilarante est survenue :")
            traceback.print_exc()

if __name__ == "__main__":
    main()
