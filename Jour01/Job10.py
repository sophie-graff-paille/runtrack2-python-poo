class Voiture():
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def setMarque(self, marque):
        self.__marque = marque
        return self.__marque
    
    def getMarque(self):
        return self.__marque
    
    def setModele(self, modele):
        self.__modele = modele
        return self.__modele
    
    def getModele(self):
        return self.__modele
    
    def setAnnee(self, annee):
        self.__annee = annee
        return self.__annee
    
    def getAnnee(self):
        return self.__annee
    
    def setKilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
        return self.__kilometrage
    
    def getKilometrage(self):
        return self.__kilometrage
    
    def setEnMarche(self, en_marche):
        self.__en_marche = en_marche
        return self.__en_marche
    
    def getEnMarche(self):
        return self.__en_marche
    
    def setReservoir(self, reservoir):
        self.__reservoir = reservoir
        return self.__reservoir
    
    def getReservoir(self):
        return self.__reservoir
    
    def demarrer(self):
        self.__en_marche = True
        if self.__reservoir > 5:
            return False
    
    def arreter(self):
        self.__en_marche = False
        return self.__en_marche
    
    def verifier_plein(self):
        return self.__reservoir
    
voiture = Voiture("Nissan", "Juke", 2015, 100000)
print(voiture.getMarque(), voiture.getModele(), voiture.getAnnee(), voiture.getKilometrage())
print(voiture.getEnMarche())
print(voiture.getReservoir())
print(voiture.demarrer())
print(voiture.arreter())
print(voiture.verifier_plein())