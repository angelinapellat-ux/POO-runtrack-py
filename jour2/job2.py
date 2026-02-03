class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre 
        self.__auteur = auteur 
        self.__nb_pages = nb_pages 

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur 
    
    def getNbpages(self):
        return self.__nb_pages

    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre  

    def setAuteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def setNbpages(self, nouveau_nb_pages):
        if isinstance (nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else : 
            print("Erreur de page")


livre = Livre("Odyssée", "Homère", 350)

print(livre.getTitre())
print(livre.getAuteur())
print(livre.getNbpages())

livre.setTitre("Odyssée")
livre.setAuteur("Homère")
livre.setNbpages(511)

print(livre.getTitre())
print(livre.getAuteur())
print(livre.getNbpages())

#livre.setNbpages(-50) a tester pour une eventuelle erreur  

        