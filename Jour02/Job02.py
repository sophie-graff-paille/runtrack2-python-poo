class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        Personne.__init__(self)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours de", self.__matiereEnseignee, "va commencer")

personne1 = Personne
eleve1 = Eleve()
professeur1 = Professeur("Français")
eleve1.afficherAge()
eleve1.bonjour(), eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.affichageAge()
professeur1.bonjour(), professeur1.enseigner()
professeur1.modifierAge(40)
professeur1.afficherAge()