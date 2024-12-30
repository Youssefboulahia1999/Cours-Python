#coding:utf-8
#pour la documentation
#help(str)

ma_chaine = "bonjour super tout le monde. en revoir"

ma_chaine = ma_chaine.upper()#tous en majuscule
print(ma_chaine)
ma_chaine = ma_chaine.lower()#tous en minuscule
print(ma_chaine)
ma_chaine = ma_chaine.capitalize()#premier lettre en majuscule
print(ma_chaine)
ma_chaine = ma_chaine.title()#premier lettre ne majuscule chaque mots
print(ma_chaine)
ma_chaine = ma_chaine.center(60,"-")#met au centre le message
print(ma_chaine)
print(ma_chaine)
ma_chaine = "bonjour tout le monde. en revoir"
print(ma_chaine.find("super"))#trouver le mots et sa position
ma_chaine = "bonjour super tout le monde. en revoir"
print(ma_chaine.find("super"))#trouver le mots et sa position
print(ma_chaine.index("super"))#trouver le mots et sa position
print(ma_chaine.strip("super"))#enleve le espace inutile
print(ma_chaine.replace("on","ou",))#trouver le mots et sa position 
#"remplace" par "...." si pas tous le nombre
phrase = "magicien|10|5"
print(phrase.split("|"))#pour avoir une liste



try:
    ma_chaine = "bonjour super tout le monde. en revoir"
    print(ma_chaine.index("super"))#trouver le mots et sa position
except ValueError:
    print("je n'est pas trouvé")