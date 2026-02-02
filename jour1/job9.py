class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        return {
            "nom": self.nom,
            "prixHT": self.prixHT,
            "TVA": self.TVA,
            "prixTTC": self.CalculerPrixTTC()
        }

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.CalculerPrixTTC()

produit1 = Produit("Stylo", 2, 0.20)
produit2 = Produit("Cahier", 5, 0.20)
produit3 = Produit("Clé USB", 12, 0.20)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

print("Prix TTC produit 1 :", produit1.CalculerPrixTTC())
print("Prix TTC produit 2 :", produit2.CalculerPrixTTC())
print("Prix TTC produit 3 :", produit3.CalculerPrixTTC())

produit1.modifierNom("Stylo bleu")
produit1.modifierPrix(2.5)

produit2.modifierNom("Grand cahier")
produit2.modifierPrix(6)

produit3.modifierNom("Clé USB 32Go")
produit3.modifierPrix(15)

print("Nouveau prix TTC produit 1 :", produit1.getPrixTTC())
print("Nouveau prix TTC produit 2 :", produit2.getPrixTTC())
print("Nouveau prix TTC produit 3 :", produit3.getPrixTTC())
