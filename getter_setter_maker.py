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
            print(tab, "def get_", attribut, "(self):\n", tab, tab, "return self.", attribut, sep='', end='\n\n', file=dest)
            print(tab, "def set_", attribut, "(self, new_", attribut, "):\n", tab, tab, "self.", attribut, " = new_", attribut, sep='', end='\n\n', file=dest)
        print("\n\n\n", sep='', end="\n", file=dest)


def create_object(classe, attributs):
    """
        classe : str
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
        objets.append(classe(dico))
        objets = deepcopy(objets)
    return objets


def create_class_instance(nom_classe, attributs):
    """
        nom_classe : str
        attributs : {str: [], ...}
    """

    # On récupère le nom des attributs sous de string où les attributs sont séparés par des ,
    liste_attributs = ''
    for key in attributs:
        liste_attributs += (key + ',')

    # On vérifie si la classe existe déja. Sinon on la créé. En tout cas on l'importe
    try:
        exec("try:\n\tfrom classes import " + nom_classe)
    except:
        # liste
        from os import system
        system("python class_creator.py " + nom_classe + ' ' + liste_attributs)
        exec("from classes import " + nom_classe)

    # On créé la liste d'objets demandée
    objets = eval("create_object(" + nom_classe + ", attributs)")
    return objets


if __name__ == "__main__":
    # create_class(nom_classe="Pion", input_attributs="nom,position")
    # from classes import Pion
    # objets = create_object("Test", {"nn": ["pion1", "pion2"], "gg": [1, 2]})
    # print(objets[1].get_nn(), objets[0].get_gg())
    # # from os import remove
    # # remove("classes/pion.py")
    o = create_class_instance("Test", {"nom": ["pion1", "pion2"], "position": [1, 2]})
    print(o[0].get_nom(), o[1].get_position())
    # create_class(True)
    # create_class(nom_classe="Test", input_attributs=["nom", "prenom"])
