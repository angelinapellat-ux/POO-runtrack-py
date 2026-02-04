class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def getSolde(self):
        return self.__solde

    def getNumero(self):
        return self.__numero

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getDecouvert(self):
        return self.__decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero} - {self.__prenom} {self.__nom} - Solde : {self.__solde} € - Découvert autorisé : {self.__decouvert}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Erreur : fonds insuffisants pour effectuer ce retrait.")

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05   # 5% d'agios
            print(f"Agios appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, reference, compte_destinataire, montant):
        print(f"Tentative de virement '{reference}' de {montant} € vers {compte_destinataire.getPrenom()} {compte_destinataire.getNom()}")

        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Erreur : solde insuffisant pour effectuer le virement.")

compte1 = CompteBancaire(101, "Dupont", "Alice", 500, decouvert=False)

compte1.afficher()
compte1.afficherSolde()

compte1.versement(200)
compte1.retrait(100)
compte1.afficherSolde()

compte2 = CompteBancaire(202, "Martin", "Bob", -200, decouvert=True)

compte2.afficher()
compte2.agios()  # Appliquer des agios sur solde négatif
compte2.afficherSolde()

compte1.virement("Remboursement découvert", compte2, 300)

compte1.afficher()
compte2.afficher()

