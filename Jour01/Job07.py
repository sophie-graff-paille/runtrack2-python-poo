class Livre():
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages

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
    
livre = Livre("Avenue des Mystères", "John Irving", 605)
print(livre.getTitre(), ", ", livre.getAuteur(),", ", livre.getNbPages())
livre.setNbPages(-10)
print(livre.getNbPages())
livre.setNbPages(604)
print(livre.getNbPages())