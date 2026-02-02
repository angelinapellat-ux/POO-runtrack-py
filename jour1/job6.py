class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ''

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


animal = Animal()

print("Âge de l'animal :", animal.age)

animal.vieillir()
print("Âge de l'animal :", animal.age)

animal.nommer("Luna")
print("Nom de l'animal :", animal.prenom)


