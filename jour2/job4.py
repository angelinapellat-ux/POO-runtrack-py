class Student:
    def __init__(self, nom, prenom, student_id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = student_id
        self.__credits = 0
        self.__level = self.__studentEval()   

    def add_credits(self, nb):
        if isinstance(nb, int) and nb > 0:
            self.__credits += nb
            self.__level = self.__studentEval()   
        else:
            print("Erreur : le nombre de crédits doit être un entier positif.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("ID :", self.__id)
        print("Niveau :", self.__level)

    def getCredits(self):
        return self.__credits

etudiant = Student("Doe", "John", 145)

etudiant.add_credits(20)
etudiant.add_credits(15)

print("Total de crédits :", etudiant.getCredits())

etudiant.studentInfo()

