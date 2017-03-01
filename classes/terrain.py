class Terrain:

    def __init__(self, attributs):
        self.attr = attributs
        self.set_prix_d_achat_maison(attributs["prix_d_achat_maison"])
        self.set_prix_d_achat(attributs["prix_d_achat"])
        self.set_nom(attributs["nom"])

    # Gestion de prix_d_achat_maison
    def get_prix_d_achat_maison(self):
        return self.prix_d_achat_maison

    def set_prix_d_achat_maison(self, new_prix_d_achat_maison):
        self.prix_d_achat_maison = new_prix_d_achat_maison

    # Gestion de prix_d_achat
    def get_prix_d_achat(self):
        return self.prix_d_achat

    def set_prix_d_achat(self, new_prix_d_achat):
        self.prix_d_achat = new_prix_d_achat

    # Gestion de nom
    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom


