#coding:utf-8
"""
mode d'ouverture:
    r (lecture seul)
    w (ecriture avec replacement)
    a (ecriture avec ajout en fin de fichiers)
    r+ (lecture ecriture dans un meme fichiers)

"""

#ouvrire le ficher et le fermer
fic = open("15.txt","r")
#lire le fichier
print(fic.read())
#fermer
fic.close()

with open("15.txt","r") as fic:
    content = fic.read()
    print(content)



#ici le fichiers s'ouvre que dans le with 
with open("15.txt","w") as fic:
    nombre = 15
    fic.write(str(nombre))



if fic.close():
    print("le fichiers est fermer")
else:
    print("le fichier est ouvert")
