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

p = Personne()

e = Eleve()

e.afficherAge()

