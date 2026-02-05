class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.getLongueur() * self.getLargeur() * self.__hauteur

rect = Rectangle(10, 5)

print("Longueur :", rect.getLongueur())
print("Largeur :", rect.getLargeur())
print("Périmètre :", rect.perimetre())
print("Surface :", rect.surface())

rect.setLongueur(20)
rect.setLargeur(8)

print("\nAprès modification :")
print("Longueur :", rect.getLongueur())
print("Largeur :", rect.getLargeur())
print("Périmètre :", rect.perimetre())
print("Surface :", rect.surface())

p = Parallelepipede(10, 5, 3)
print("\nVolume du parallélépipède :", p.volume())
	

