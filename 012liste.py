#coding:utf-8


#cree des liste 
inventaire0=[]
inventaire = list()
inventaire1 = [1,15,198,"voiture"] * 3
inventaire2 = range(20)#pour le lire il faut une boucle
inventaire3 = ["arc", "epee", "bouclier","hache","baton","tunique"]
i = 0

#boucle pour lire les liste
while i < len(inventaire2):
    print(inventaire2[i])
    i += 1

#ont donne pour chaque valeur un inventer
for valeur in inventaire3:
    print(valeur)

for objet in enumerate(inventaire3):
    print(objet)

for indice_objet, valeur_objet in enumerate(inventaire3):
    print("element d'indice {} -> {}".format(indice_objet, valeur_objet))

for k, v in enumerate(inventaire3):
    print("element d'indice {} -> {}".format(k, v))

#modification
inventaire3[2] = "bouclier d'acier"
inventaire3[:]= ["bouclier d'acier"] * len(inventaire3)#change tous les l'element par 
print(inventaire3[:])#tous lire 
inventaire3[:] = ["bouclier d'acier"]*2
inventaire3 = ["arc", "epee", "bouclier","potion","potion","hache","baton","tunique"]


#affichage de liste
print(inventaire1)#tous lire
print(inventaire3[:])#tous lire 
print(inventaire3[2])#lire l'indeice 2
print(inventaire3[:3])#les deux premier
print(inventaire3[1:])#les deux dernier
print(inventaire3[-2])#deuxieme indice en partant de la fin
print(inventaire3[2:4])#affiche l'element de 2 a 4

#voir si un element est dedans 
if "bouclier" in inventaire3:
    print("j'ai un bouclier")
else:
    print("je n'en ai pas")

#ajouter un element
inventaire0.append("arc")
inventaire0.insert(1,"potion mana")#insert a un indice dit
print(inventaire0)

#supprimer 
del inventaire0[1]
inventaire0.remove("arc")
print(inventaire0)

#donne l'index
print("Indice :", inventaire3.index("bouclier"))

#trier chiffre ou lettre
inventaire3.sort()#croissan
inventaire3.reverse()#decroissance
print("nombre de potion:", inventaire3.count("potion"))
print(inventaire3)

#effacer la liste
inventaire3.clear()
inventaire3[:] = []

#liste a chaine <=>
chaine = "bonjour a tous" 
chaine = chaine.split(" ")
inventairee = ["bonjour", "a", "tous"]
phrase = " ".join(inventairee)
print(phrase)

#fusionner deux liste
inventaire0 = inventaire0 + inventaire1
inventaire0 += inventaire1

#help(list)
print(phrase)
print(inventaire0)
premier_tableau = [1, 2, 3, 4]
deuxieme_tableau = ["_", "_", "_", 2]

# Créer un dictionnaire avec des paires d'éléments correspondants
dictionnaire_combine = {}
for i in range(min(len(premier_tableau), len(deuxieme_tableau))):
    dictionnaire_combine[i] = (premier_tableau[i], deuxieme_tableau[i])

# Afficher le dictionnaire résultant
print(dictionnaire_combine)