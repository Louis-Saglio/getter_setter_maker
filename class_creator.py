from sys import argv

nom_classe = argv[1]
tab = '    '
input_attributs = argv[2]
if input_attributs[len(input_attributs)-1] != ',':
    input_attributs += ','

attributs = []
attr = ''
for lettre in input_attributs:
    if lettre != ',':
        attr += lettre
    else:
        attributs.append(attr)
        attr = ''

with open("classes.py", 'a') as dest:
    print("class ", nom_classe, ':\n', sep='', file=dest)
    print(tab, "def __init__(self, attributs):", sep='', file=dest)
    print(tab, tab, "self.attr = attributs", sep='', file=dest)
    for attribut in attributs:
        print(tab, tab, "self.set_", attribut, "(attributs[\"", attribut, "\"])", sep='', file=dest)
    print("\n", end='', file=dest)
    for attribut in attributs:
        print(tab, "# Gestion de ", attribut, sep='', file=dest)
        print(tab, "def get_", attribut, "(self):\n", tab, tab, "return self.", attribut, sep='', end='\n\n', file=dest)
        print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab, tab, "self.", attribut, " = new_",
              attribut, sep='', end='\n\n', file=dest)
    print("\n\n\n", sep='', end="\n", file=dest)