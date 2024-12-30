#integer sont les nombre entier ex: 9, 0,-9
#Float sont les nombres a virgule ex: 887.93, 6.0 873.0

#print affiche les donnees dans la console python est un langage interprete donc
#le code est traduit au moment de l'exécution ligne par ligne
print(5)
print(9.35)
print(123456)

#Une valeur est le résultat final. 
#Une expression est un calcul ou une combinaison qui produit une valeur.
print(1+2)
#dans le cas ou une expression est in float alors la valeur la sera aussi
print(18-6.7)
print(9*8)
print(8.2*27)
#dans le cas une c'est une division alors dans tous les cas valeur seront 
# des float
print(63/2)
#le regrouppement d'operation ()
print((4-5)*(5+3)/2)

#sting est une chaine de caracteres "je m'appelle"
print("Je m'appelle")
#affectation de variable
name = "Youssef"
age = 23
first_name = "Boulahia"
prix_heure = 12
heures_travail = 40
print(prix_heure * heures_travail)

#Pour obtenir des valeurs de l'utilisateur 
ut = input("donne moi ton age : ")
print(ut)

#concatenation 
print("Ton age est : " + ut)

#convertion des int str float
age = str(30)
age = int(30)
age = float(30)

#interpolation de chaine avec la methode format
print( "{} a {} ans".format('youssef',23))


output = "{0} a {1} ans et {0} travaille en tant que {2}"
print (output. format("youssef", 24, "data scientist"))
"Selina a 24 ans et Selina travaille en tant que data scientist."

output = "{name} a {age} ans et {name} travaille en tant que {job}"
print (output. format(name="youssef",age=24, job="data scientist"))
"Selina a 24 ans et Selina travaille en tant que data scientist."
print(f"{name} a {age} ans !")
print("ndjje djjs  jj ".strip().title())