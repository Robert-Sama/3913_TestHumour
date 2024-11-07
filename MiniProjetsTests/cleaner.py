with open("test.lol", "r") as file:
    lines = file.readlines()

# Supprimer les espaces en début de chaque ligne
cleaned_lines = [line.lstrip() for line in lines]

with open("test.lol", "w") as file:
    file.writelines(cleaned_lines)

with open("test.lol", "r") as file:
    content = file.read()

# Affiche tous les caractères non standards avec leurs positions
for i, char in enumerate(content):
    if not (char.isascii() and char.isprintable()):
        print(f"Caractère non standard à la position {i}: {repr(char)}")

with open("test.lol", "r") as file:
    content = file.read()

# Remplace tous les types d'espaces par des espaces standards
content = content.replace('\u00A0', ' ').replace('\u200B', ' ')  # Remplacer tout type d'espace non standard

with open("test.lol", "w") as file:
    file.write(content)
