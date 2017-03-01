class Joueur:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_position(attributs["position"])
        self.set_nom(attributs["nom"])

    # Gestion de position
    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom


