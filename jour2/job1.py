class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

rect = Rectangle(10, 5)

print("Longueur :", rect.getLongueur())
print("Largeur :", rect.getLargeur())

rect.setLongueur(20)
rect.setLargeur(8)

print("Nouvelle longueur :", rect.getLongueur())
print("Nouvelle largeur :", rect.getLargeur())
