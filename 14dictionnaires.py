#coding:utf-8
#dictionnaire est un tableau associatif

dico = {
    "prenom":"youssef",
    "nom":"boulahia",
    "age":"23"
}
print(dico["prenom"])

#ajoute une cle associatif
dico["chien"]= "c'est un mamifere"

#suppression
del dico["nom"]
dico.pop("prenom")

#trouve seulement les clef assos
if "age" in dico:
    print("oui")
else:
    print("non")

#copie un dico
dico1 = dico.copy()
print(dico1)

#parcourir 
for v in dico.keys():
    print(v)

for v in dico.values():
    print(v)

for v,k in dico.items():
    print("la cle {} a pour valeur {}".format(v,k))

for v in dico:
    print(v)


def maFonction(**parametre):
    print(parametre)

maFonction(chiffre=1584, nom="blabla")
print(dico)
