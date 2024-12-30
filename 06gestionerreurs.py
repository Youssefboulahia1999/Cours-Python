#coding:utf-8
ageUtilisateur = input("quel age a tu ?")

""" 
    try esseil le code 
    except sont les exeption quand le test est incorrect
    esle permet la suite du code si tous est bon
    fanally sont les code a executer peut import les erreurs

 """

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("l'age indique est incorrect ")
else:
    print("tu as", ageUtilisateur,"ans")
finally: 
    print("fin du programme...")
  

""" des except en fonction des erreur """
nombre1 = 450
nombre2 = input("choisir une nombre pour diviser : ")

try:
    nombre2 =int(nombre2)
    print("resulta = {}".format(nombre1/nombre2))
except ZeroDivisionError:
    print("vous ne pouvez pas diviser par zero.")
except  ValueError:
    print ("vous devez entrer un nombre.")
except:
    ("valeur incorrect")

try:
    age = input("quel age a tu")
    age = int(age)

    assert age < 25:#chemin si age < 25 
except AssertionError:
    print("")