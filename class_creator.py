from sys import argv
from os.path import isdir
from os import system

# On récupère les arguments
nom_classe = argv[1]
tab = '    '
attributs = argv[2].split(',')

# On vérifie que le dossier classes existe, sinon on le créé
if not isdir("classes"):
    system("mkdir classes")

# On créé et ouvre le fichier de la classe
with open("classes/" + nom_classe.lower() + ".py", 'a') as dest:

    # Class nom_classe:
    print("class ", nom_classe, ':\n', sep='', file=dest)

    # Ecriture de __init__
    print(tab, "def __init__(self, attributs):", sep='', file=dest)
    print(tab * 2, "self.attr = attributs", sep='', file=dest)
    for attribut in attributs:
        print(tab * 2, "self.set_", attribut, "(attributs[\"", attribut, "\"])", sep='', file=dest)
    print(tab * 2, "# Attention ! Toujours laisser la ligne suivante a la fin de la methode init\n", tab * 2,
          "# Fin de la methode init",
          sep='', file=dest)
    print("\n", end='', file=dest)

    # Ecriture des getters et setters
    for attribut in attributs:
        print(tab, "# Gestion de ", attribut, sep='', file=dest)
        print(tab, "def get_", attribut, "(self):\n", tab * 2, "return self.", attribut, sep='', end='\n\n', file=dest)
        print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab * 2, "self.", attribut, " = new_",
              attribut, sep='', end='\n\n', file=dest)
