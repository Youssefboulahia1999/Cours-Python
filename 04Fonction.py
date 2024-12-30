#coding:utf-8
"""
fonction :print(), input(), type(), int(), 
une fonction commence par sa definition donc "def" """

print("bonjour a tous ! :)")

def dire_bonjour():
    print("bonjour tout le monde")

dire_bonjour()


""" une fonction avec et sans parametre par defaut"""
def dire(nom_personne="tom", message_personne="salut", age=18):
    print("{} ({} ans): {}".format(nom_personne,age,message_personne))
dire("youssef","bonjour a tous")
dire("tom","salut")
dire(nom_personne="jason",age="26")

print(dire())

"""fonction avec des argument infinie"""
def inventory(*liste_items):
    for item in liste_items:
        print(item)

inventory("epee")
inventory("arc","potion","cape")


""""une fonction avec plusieur return """
def calculer (nombre1,nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "egalité !"

    resultat = nombre1 + nombre2
    return resultat

