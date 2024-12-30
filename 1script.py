#coding:utf-8
"""
commentaire /n
une variable doir commencer par une lettre
sans caractere speciaux 
sans espace
langage dynamique le langage laisse libre court a type pas besoin de int
string booleen avant la variable

type de donnees 
(int)
(float)
(str)
(bool)
"""
print("bonjour \ntout le monde")
#
agePersonne = 14
prix = "15"

print(type(agePersonne))
print(type(prix))
print("age de la personne :", agePersonne)

texte = "l'age de la personne est {} et le prix ht est de {}€."
print(texte.format(agePersonne,prix))

ageJoueur = input("choisissez le age de joueur")
print("age", nomJoueur)
ageJoueur = int(ageJoueur)
