class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes=0, jaunes=0, rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print(f"Joueur : {self.nom} | Numéro : {self.numero} | Position : {self.position}")
        print(f"Buts : {self.buts} | Passes décisives : {self.passes}")
        print(f"Cartons jaunes : {self.jaunes} | Cartons rouges : {self.rouges}")
        print("-" * 40)

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}")
        print("=" * 40)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return
        print("Joueur introuvable dans l'équipe.")

equipeA = Equipe("Tigres")
equipeB = Equipe("Lions")

j1 = Joueur("Alex", 9, "Attaquant")
j2 = Joueur("Marco", 10, "Milieu")
j3 = Joueur("Leo", 1, "Gardien")

j4 = Joueur("Sam", 7, "Attaquant")
j5 = Joueur("Nico", 4, "Défenseur")

equipeA.ajouterJoueur(j1)
equipeA.ajouterJoueur(j2)
equipeA.ajouterJoueur(j3)

equipeB.ajouterJoueur(j4)
equipeB.ajouterJoueur(j5)

print("\n--- Statistiques AVANT le match ---")
equipeA.afficherStatistiquesJoueurs()
equipeB.afficherStatistiquesJoueurs()

equipeA.mettreAJourStatistiquesJoueur("Alex", "but")
equipeA.mettreAJourStatistiquesJoueur("Marco", "passe")
equipeB.mettreAJourStatistiquesJoueur("Sam", "rouge")
equipeA.mettreAJourStatistiquesJoueur("Leo", "jaune")

print("\n--- Statistiques APRÈS le match ---")
equipeA.afficherStatistiquesJoueurs()
equipeB.afficherStatistiquesJoueurs()

