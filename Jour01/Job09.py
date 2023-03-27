class Student():
    def __init__(self, prenom, nom, id, credits, level):
        self.__prenom = prenom
        self.__nom = nom
        self.__id = id
        self.__credits = credits
        self.__level = level

    def setPrenom(self, prenom):
        self.__prenom = prenom
        return self.__prenom
    
    def getPrenom(self):
        return self.__prenom
    
    def setNom(self, nom):
        self.__nom = nom
        return self.__nom
    
    def getNom(self):
        return self.__nom
    
    def setId(self, id):
        self.__id = id
        return self.__id
    
    def getId(self):
        return self.__id
    
    def setCredits(self, credits):
        self.__credits = credits
        return self.__credits

    def getCredits(self):
        return self.__credits
    
    def add_credits(self, credits):
        self.__credits += credits
        if self.__credits < 0:
            print("Attention ! Le nombre de crédits ne peut pas être négatif")
        else:
            print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credits)
        
    def studentEval(self):
        if self.__credits >= 90:
            print("Excellent")
        elif self.__credits >= 80:
            print("Très bien")
        elif self.__credits >= 70:
            print("Bien")
        elif self.__credits >= 60:
            print("Passable")
        elif self.__credits < 60:
            print("Insuffisant")
        else:
            print("Erreur")

    def studentInfo(self):
        print("Nom =", self.__nom)
        print("Prénom =", self.__prenom)
        print("Id =", self.__id)
        print("Niveau =", self.__level)

credits = 0
student = Student("John", "Doe", 145, 0, "Bien")
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)
student.add_credits(45)
level = student.studentEval()
student.studentInfo()