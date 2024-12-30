# #coding:utf-8

class Humain:

    lieu_habitation = "terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):  # methode standard
        print("{} a dit {}".format(self.nom, message))

    """methode de class qui permet de changer un attribut de la class"""
    # methode de classe 
    def changer_planete(cls, nouvelle_planete):
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)

    def definition():
        print("l'humain est classe comme etanta")

    definition = staticmethod(definition)


h1 = Humain("jason", 26)
""" si il n'y a pas d'objet cree la methode ne marche pas c'est grace 
a l'inctanciation que les info du message existe"""
h1.parler("boujour")

print("planete actuelle {}".format(Humain.lieu_habitation))

Humain.changer_planete("Mars")

print("planete actuelle {}".format(Humain.lieu_habitation))
