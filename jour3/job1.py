class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def getNom(self):
        return self.__nom

    def getNbHabitants(self):
        return self.__nb_habitants

    def ajouterHabitant(self):
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouterHabitant()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print("Population de la ville de Paris :", paris.getNbHabitants())
print("Population de la ville de Marseille :", marseille.getNbHabitants())

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print("Mise à jour de la population de la ville de Paris :", paris.getNbHabitants())
print("Mise à jour de la population de la ville de Marseille :", marseille.getNbHabitants())
