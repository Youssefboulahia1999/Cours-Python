#coding:utf-8
"""
import math   permet d'import certaines fonction de math
si vous mettez import vous devez appeler le nom de la fonction

from math import .... * donne un nom du ficher "math"
 et import ce que tu veux, si c'est un from alors pas 
 besoin d'appeler la fonction par le from

"""
coucou = lambda:print("bonjour")
coucou()

""" """
ttc = lambda prixHT: prixHT + (prixHT * 20 /100)
print(ttc(24))
""" """
calculer = lambda a,b: a + b
print(calculer(14,27))
"""  """
import math 

resultat = math.sqrt(100)

print(resultat)

sinus = math.sin(42)
print(sinus)
"""   """
from math import *

resultat = sqrt(100)
print(resultat)
""" """
from _5player import *

au_revoir()
parler("youssef","salut les abonnes !")

""" si le module est dans un autre ficher alors
mettre les ficher puis . puis ficher
le as permet d'appeler le fonction par le as  """
import includes.player as player

player.au_revoir()
player.parler("youssef","salut les abonnes !")
