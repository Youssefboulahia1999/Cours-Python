#coding:utf-8

compteur = 0
while compteur < 5:
    compteur += 1
    print("je suis une prase", compteur)
print ("je suis sortie de la boucle ")

""" """
jeu = True
while jeu:

    choixmenu = input("> ")
    
    if choixmenu == "again":
        continue 
    elif choixmenu == "quit":
        jeu = False
    elif choixmenu == "hello":
        print("bonjour")
    else:
        print("commande introuvable")
print("a bientot...")



phrase = "bonjour tout le monde"



for letter in phrase:
    print(letter)

print("a bientot...")

premier_tableau = [1, 2, 3, 4]
deuxieme_tableau = ["_", "_", "_", 2]

# Créer un dictionnaire avec des paires d'éléments correspondants
dictionnaire_combine = {}
for i in range(min(len(premier_tableau), len(deuxieme_tableau))):
    dictionnaire_combine[i] = (premier_tableau[i], deuxieme_tableau[i])

# Afficher le dictionnaire résultant
print(dictionnaire_combine)
