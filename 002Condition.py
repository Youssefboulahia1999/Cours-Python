#coding:utf-8
""" 
operateur: + - * / %

"""
calcul = 5/2
calcul = int(calcul)

print("resulta" , calcul)

""""                  """


"""
operateur de comparaison: == != <  > <= >=
condition multiples:  and or in / not in
 """
idantifant = "youssef"
motdepasse = "123"

print("interface de connection")

user_id = input("entrez votre idantifiant :")
user_motdepasse = input("entrez votre mot de passe:")

if user_id == idantifant and user_motdepasse == motdepasse:
    print("vous etes connectes, bienvenue", user_id)

print("endehors")

"""     """
lettre_hasard = "b"
if lettre_hasard in "aeiouy":
    print("c'est une voyelle")
else:
    print("c'est une consonne")
"""  """
age = 50
if age == 18:
    print("tu vien d'etre majeur")
elif age == 50:
    print("tu as 50 ans")
else:
    print("tu as",age,"ans") 
""" """
jeu = False

if not jeu:
    print("jeu eteint")
else:
    print("le jeu lancé")
""" """

if 0 < age <= 100:
    print("l'age est valide")
else:
    print("l'age n'est pas valide") 
