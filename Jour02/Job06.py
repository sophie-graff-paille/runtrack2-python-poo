class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Année = ", self.annee)
        print("Prix = ", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de portes = ", self.portes)

    def demarrer(self):
        print("Faites gaffe, je roule aussi !")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print("Nombre de roues = ", self.roues)

    def demarrer(self):
        print("Ecartez-vous, je suis la plus rapide !!")

vehicule1 = Vehicule("Nissan", 2015, 10000)
vehicule1.demarrer()
voiture1 = Voiture("Mercedes", 2020, 18500)
voiture1.informationsVehicule()
voiture1.demarrer()
moto1 = Moto("Yamaha", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()