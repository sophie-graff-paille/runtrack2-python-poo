class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setRectangle(self, longueur):
        self.__longueur = longueur
        return self.__longueur

    def getLongueur(self):
        return self.__longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def getLargeur(self):
        return self.__largeur
    
rectangle = Rectangle(10, 5)
print(rectangle.getLongueur(),", ", rectangle.getLargeur())
rectangle.setRectangle(20)
rectangle.setLargeur(10)
print(rectangle.getLongueur(),", ", rectangle.getLargeur())