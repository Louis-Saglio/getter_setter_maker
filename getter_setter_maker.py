from write_in_file import insert_line_into_file, iter_file


def create_class(verbose=False, nom_classe=None, input_attributs=None, tab='    '):
    if verbose:
        nom_classe = input("Entrez le nom de la classe: ")
        input_attributs = input("Entrez le nom des attributs séparés par des virgules:  ")
        input_attributs += ','
        attributs = []
        attr = ''
        for lettre in input_attributs:
            if lettre != ',':
                attr += lettre
            else:
                attributs.append(attr)
                attr = ''
    attributs = input_attributs

    with open("classes.py", 'a') as dest:
        print("class ", nom_classe, ':\n', sep='', file=dest)
        print(tab, "def __init__(self, attributs):", sep='', file=dest)
        print(tab, tab, "self.attr = attributs", sep='', file=dest)
        for attribut in attributs:
            print(tab, tab, "self.set_", attribut, "(attributs[\"", attribut, "\"])", sep='', file=dest)
        print("\n", end='', file=dest)
        for attribut in attributs:
            print(tab, "# Gestion de ", attribut, sep='', file=dest)
            print(tab, "def get_", attribut, "(self):\n", tab, tab, "return self.", attribut, sep='', end='\n\n',
                  file=dest)
            print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab, tab, "self.", attribut, " = new_",
                  attribut, sep='', end='\n\n', file=dest)
        print("\n\n\n", sep='', end="\n", file=dest)


def create_object(classe, attributs):
    """
        classe : Type
        attributs : {str: [], ...}
    """

    # On initialise les éléments
    from copy import deepcopy
    objets = []
    noms_attr = []
    dico = {}

    # On créé un dictionnaire de liste avec le nom des attributs comme clé
    for key in attributs:
        noms_attr.append(key)
        dico[key] = []

    # On rempli les listes du dictionnaire avec les valeur correspondantes
    for i in range(len(attributs[noms_attr[0]])):
        for n in noms_attr:
            dico[n] = attributs[n][i]
        objets.append(classe(dico))  # Le constructeur de la classe prend un dictionnaire en paramètre
        objets = deepcopy(objets)
    return objets


def create_class_instance(nom_classe, attributs):
    """
        nom_classe : str
        attributs : {str: [], ...}
    """

    # On récupère le nom des attributs sous forme de string où les attributs sont séparés par des ,
    liste_attributs = ','.join(attributs)

    # On vérifie si la classe existe déja. Sinon on la créé. En tout cas on l'importe
    try:
        exec("from classes." + nom_classe.lower() + " import " + nom_classe)
    except ImportError:
        from os import system
        system("python class_creator.py " + nom_classe + ' ' + liste_attributs)
        exec("from classes." + nom_classe.lower() + " import " + nom_classe)

    # On créé la liste d'objets demandée
    objets = eval("create_object(" + nom_classe + ", attributs)")
    return objets


def add_attribute_to_class(nom_classe, nom_attribut, tab="    "):

    def find_right_line(class_name):
        for line in iter_file("classes/" + class_name.lower() + ".py"):
            if line["text"] == tab * 2 + "# Fin de la methode init\n":
                return line["line_num"] - 2

    print(find_right_line(nom_classe))
    insert_line_into_file("classes/" + nom_classe.lower() + '.py',
                          tab * 2 + "self.set_" + nom_attribut + "(attributs[\"" + nom_attribut + "\"])\n",
                          find_right_line(nom_classe))
    comment = tab + "# Gestion de " + nom_attribut + "\n"
    getter = tab + "def get_" + nom_attribut + "(self):\n" + tab * 2 + "return self." + nom_attribut
    setter = "\n\n" + tab + "def set_" + nom_attribut + "(self, new_" + nom_attribut + "):\n"\
        + tab * 2 + "self." + nom_attribut + " = new_" + nom_attribut
    with open("classes/" + nom_classe.lower() + ".py", 'a') as file:
        file.write(comment + getter + setter)


if __name__ == "__main__":
    o = create_class_instance("Test2", {"nom": ["pion1", "pion2"], "position": [1, 2]})
    print(o[0].get_nom(), o[1].get_position())
    add_attribute_to_class("Test2", "couleur")
