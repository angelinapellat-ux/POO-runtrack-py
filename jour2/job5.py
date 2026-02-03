class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50   

    def getMarque(self):
        return self.__marque

    def getModele(self):
        return self.__modele

    def getAnnee(self):
        return self.__annee

    def getKilometrage(self):
        return self.__kilometrage

    def getEnMarche(self):
        return self.__en_marche

    def getReservoir(self):
        return self.__reservoir

    def setMarque(self, marque):
        self.__marque = marque

    def setModele(self, modele):
        self.__modele = modele

    def setAnnee(self, annee):
        self.__annee = annee

    def setKilometrage(self, km):
        self.__kilometrage = km

    def setReservoir(self, niveau):
        self.__reservoir = niveau

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Impossible de démarrer : réservoir faible.")

    def arreter(self):
        self.__en_marche = False

v = Voiture("Audi", "TTRS", 2014, 45000)

print("En marche :", v.getEnMarche())

v.demarrer()
print("En marche après démarrage :", v.getEnMarche())

v.setReservoir(3)

v.arreter()
v.demarrer()  

print("En marche :", v.getEnMarche())

