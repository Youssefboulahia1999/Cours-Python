#coding:utf-8

""" programmation orrienter objet poo """
""" 
classe : est un plan un ensempble qui sera definit par
des methode, propriete, des attribut  (ex:humain)

objet : est une insatance d une classe, une antiter
qui fait partie d une classe insatanssier une classe
et la creation d un objet (ex:youssef)

un attribut : est une variable d une classe 
(ex: ex ,taille,couleur)
propriete : est une maniere de manipuler les attribut
(ex:prive, lecture seule)

methode : fonction d une classe (marcher, manger ect)
methode de classe : fonction d une classe
methode statique : fonction d une classe independante

heritage : classe fille qui heritte d une classe mere 
classe chat herite de classe animal """

class   Humain:
    """ self est la difinition ou l'identifian de l'objet
    les parametre 
    """
    """ humain creas est un nombre qui peut conrespondre a l'id pour 
    chaque humain cree +1 """
    humain_creas = 0

    def __init__(self,c_prenom="toto",c_age="19"):
        print("creation d'un humain", self)
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_creas += 1
"""donne des attribut par defaut 
        self.prenom = "jojo"
        self.age = 1"""

print("lancement du programme...")

h1 = Humain("jojo",34)
print("prenom de h1 {}".format(h1.prenom))
print("age de h1 {}".format(h1.age))
h2 = Humain("albert", 17)
print("prenom de h1 {}".format(h2.prenom))
print("age de h1 {}".format(h2.age))
print ("humain creee {}".format(Humain.humain_creas))