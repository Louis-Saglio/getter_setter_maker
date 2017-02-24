nom_classe = input("Entrez le nom de la classe: ")
input_attributs = input("Entrez le nom des attributs séparés par des virgules:  ") + ','
tab = "    "

attributs = []
attr = ''
for lettre in input_attributs:
    if lettre != ',':
        attr += lettre
    else:
        attributs.append(attr)
        attr = ''

print("class ", nom_classe, ':\n', sep='', file=open(nom_classe.lower() + '.py', 'w'))
print(tab, "def __init__(self):", sep='', file=open(nom_classe.lower() + '.py', 'a'))
for attribut in attributs:
    print(tab, tab, "self.", attribut, " = \"Undefined\"", sep='', file=open(nom_classe.lower() + '.py', 'a'))
print("\n", end='', file=open(nom_classe.lower() + '.py', 'a'))
for attribut in attributs:
    print(tab, "# Gestion de ", attribut, sep='', file=open(nom_classe.lower() + '.py', 'a'))
    print(tab, "def get_", attribut, "(self):\n", tab, tab, "return self.", attribut, sep='', end='\n\n', file=open(nom_classe.lower() + '.py', 'a'))
    print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab, tab, "self.", attribut, " = new_", attribut, sep='', end='\n\n', file=open(nom_classe.lower() + '.py', 'a'))
