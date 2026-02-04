class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut  

    def __repr__(self):
        return f"{self.titre} - {self.description} ({self.statut})"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"

    def afficherListe(self):
        return self.taches

    def filterListe(self, statut):
        return [t for t in self.taches if t.statut == statut]


t1 = Tache("Courses", "Acheter du lait et du pain")
t2 = Tache("Sport", "Faire 30 minutes de course")
t3 = Tache("Lecture", "Lire 20 pages du livre")

liste = ListeDeTaches()

liste.ajouterTache(t1)
liste.ajouterTache(t2)
liste.ajouterTache(t3)

liste.supprimerTache("Sport")

liste.marquerCommeFinie("Lecture")

print("Toutes les tâches :")
print(liste.afficherListe())

print("\nTâches à faire :")
print(liste.filterListe("à faire"))
