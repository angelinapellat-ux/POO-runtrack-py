class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"Age : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J’ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiere, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")

eleve = Eleve()

eleve.bonjour()

eleve.allerEnCours()

eleve.modifierAge(15)

eleve.afficherAge()

prof = Professeur("Mathématiques", age=40)

prof.bonjour()

prof.enseigner()
