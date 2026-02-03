class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__plats = {}   
        self.__statut = "en cours"

    def getNumero(self):
        return self.__numero

    def getPlats(self):
        return self.__plats.copy()

    def getStatut(self):
        return self.__statut

    def setStatut(self, nouveau_statut):
        if nouveau_statut in ["en cours", "terminée", "annulée"]:
            self.__statut = nouveau_statut

    def ajouterPlat(self, nom, prix):
        self.__plats[nom] = prix

    def annulerCommande(self):
        self.__statut = "annulée"

    def __calculerTotal(self):
        return sum(self.__plats.values())

    def calculerTVA(self):
        return self.__calculerTotal() * 0.20

    def afficherCommande(self):
        total = self.__calculerTotal()
        tva = self.calculerTVA()
        total_ttc = total + tva

        print(f"Commande n°{self.__numero}")
        print("Statut :", self.__statut)
        print("Plats commandés :")

        for plat, prix in self.__plats.items():
            print(f" - {plat} : {prix} €")

        print(f"Total HT : {total} €")
        print(f"TVA (20%) : {tva} €")
        print(f"Total TTC : {total_ttc} €")

cmd = Commande(101)

cmd.ajouterPlat("Pizza Margherita", 12)
cmd.ajouterPlat("Pâtes Carbonara", 14)
cmd.ajouterPlat("Tiramisu", 6)

cmd.afficherCommande()

print("TVA :", cmd.calculerTVA())

cmd.annulerCommande()

print("Statut après annulation :", cmd.getStatut())

cmd.afficherCommande()

