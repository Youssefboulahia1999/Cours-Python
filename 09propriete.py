#coding:utf-8
"""_ sont les methode que n'ont utilise pas endehors (privé)"""
""" avant de declarer l'attribut ont le fait passer par une fonction un test car
il est en prive avec (_) sans le modifier comme sa pour le modifier il faut 
passer par la methode set_age """

class Humain:
    """cette classe """
    def __init__ (self, nom, age):
        self.nom = nom
        """_ sont les methode que n'ont utilise pas endehors (privé)"""
        self._age = age

    """#avant de declarer l'attribut ont le fait passer par 
    une fonction un test car il est en prive avec (_) sans le
     modifier comme sa pour le modifier il 
     faut passer par la methode set_age"""

    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("l'age n'existe pas")
            
    
    def _setage(self,nouvelle_age):
        if nouvelle_age < 0:
            self._age = 0
        else:
            self._age = nouvelle_age
    
    def _delage(self):
        """del permet de supprimer les donnes du self demander"""
        del self._age

#get set delet help (propriete qui manipule l'attribut)
    age = property(_getage, _setage, _delage, "je suis l'age d'un humain")

h1 = Humain("jason",26)
print(h1.age)
h1.age = 20

del h1.age
print(h1.age)
help(Humain)