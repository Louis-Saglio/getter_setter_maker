# Exemple d'utilisation de l'outil getter_setter_maker. Pour le tester, placez-le dans un dossier vierge avec les
# fichiers getter_setter_maker.py et class_creator.py puis lancez le avec Python 3.2 ou plus.

from getter_setter_maker import create_class_instance
from os import chdir

# On change dossier pour être dans le même dossier que class_creator et getter_setter_maker
chdir("..")


def creer_plateau():
    terrains = {
        "nom": [
            "Rue de la paix",
            "Avenue Henri Martin",
            "Place Pigalle",
            "Place de la Bourse"
        ],
        "prix_d_achat": [
            40000,
            28000,
            20000,
            34000
        ],
        "prix_d_achat_maison": [
            20000,
            15000,
            10000,
            15000
        ]
    }
    return create_class_instance("Terrain", terrains)


def creer_joueurs():
    joueurs = {
        "nom": [
            "Louis",
            "Patrick",
            "Jean"
        ],
        "position": [
            "Rue de la paix",
            "Avenue Henri Martin",
            "Place Pigalle"
        ]
    }
    return create_class_instance("Joueur", joueurs)


if __name__ == "__main__":
    creer_joueurs()
    for terrain in creer_plateau():
        print(terrain.get_nom(), terrain.get_prix_d_achat(), terrain.get_prix_d_achat_maison())
    print("\nVous pouvez observer qu'un dossier classes s'est créé et qu'il contient les classes demandées dans "
          "des fichiers séparés")
