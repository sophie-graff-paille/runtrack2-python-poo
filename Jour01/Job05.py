class Animal():
    def __init__(self, age):
        self.age = age
        self.prenom = ""
        print("L'age de l'animal est de", self.age, "ans")

    def vieillir(self):
        self.age += 1
        print("L'age de l'animal est de", self.age, "ans")

    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", self.prenom)

age = 0
animal = Animal(age)
animal.vieillir()
animal.nommer("Luna")