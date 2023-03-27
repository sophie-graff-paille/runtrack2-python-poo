class Livre():
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
        self.__disponible = True

    def setTitre(self, titre):
        self.__titre = titre
        return self.__titre
    
    def getTitre(self):
        return self.__titre
    
    def setAuteur(self, auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def getAuteur(self):
        return self.__auteur
    
    def setNbPages(self, nbPages):
        self.__nbPages = nbPages
        if self.__nbPages < 0:
            print("Attention ! Le nombre de pages ne peut pas être négatif")
        
    def getNbPages(self):
        return self.__nbPages
    
    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.verification() == True:
            self.__disponible == False
            print("Le livre a été emprunté")
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.verification() == False:
            self.__disponible == True
            print("Le livre a été rendu")
        else:
            print("Le livre est disponible")
        
livre = Livre("Avenue des Mystères", "John Irving", 605)
print("le livre est ", livre.verification())
livre.emprunter()
livre.rendre()