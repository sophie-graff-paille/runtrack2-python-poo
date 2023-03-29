class Forme:
    def __init__(self):
        pass

    def aire():
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius ** 2
    
forme1 = Forme
print("Ma forme a une aire de", forme1.aire(), "cm²")
rectangle1 = Rectangle(14, 8)
print("Mon rectangle a une aire de", rectangle1.aire(), "cm²")
cercle1 = Cercle(12)
print("Mon cercle a une aire de", cercle1.aire(), "cm²")