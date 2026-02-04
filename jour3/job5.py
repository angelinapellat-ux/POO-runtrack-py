class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = 10
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")

    def estVivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")

        choix = input("Votre choix : ")

        if choix == "1":
            self.niveau = "facile"
        elif choix == "2":
            self.niveau = "moyen"
        elif choix == "3":
            self.niveau = "difficile"
        else:
            print("Choix invalide, niveau facile sélectionné par défaut.")
            self.niveau = "facile"

    def lancerJeu(self):
        if self.niveau == "facile":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 60)
        elif self.niveau == "moyen":
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 100)
        else:  # difficile
            joueur = Personnage("Joueur", 80)
            ennemi = Personnage("Ennemi", 120)

        print(f"\nDébut du combat ! Niveau : {self.niveau.upper()}")
        print(f"{joueur.nom} : {joueur.vie} PV | {ennemi.nom} : {ennemi.vie} PV\n")

        while joueur.estVivant() and ennemi.estVivant():
        
            joueur.attaquer(ennemi)
            print(f"Vie de l'ennemi : {ennemi.vie}")

            if not ennemi.estVivant():
                break

            ennemi.attaquer(joueur)
            print(f"Vie du joueur : {joueur.vie}\n")

        self.verifierGagnant(joueur, ennemi)

    def verifierGagnant(self, joueur, ennemi):
        print("\n--- FIN DU COMBAT ---")
        if joueur.estVivant():
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu...")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

