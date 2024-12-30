#coding:utf-8

#classe mere
class Vehicule:
    def __init__(self,nom_vehicule,quantite_essence):
        self.nom = nom_vehicule
        self.essence= quantite_essence

    def se_deplacer(self):
        print("le vehicule {} ce deplace".format(self.nom))

#class fille
class Voiture(Vehicule):
    def __init__(self,nom_voiture,essence,puissance):
        Vehicule.__init__(self,nom_voiture,essence)
        self.puissance = puissance

    def se_deplacer(self):
        print("je roule...")

class Avion(Vehicule):
    def __init__(self,nom,essence,marchandise):
        Vehicule.__init__(self,nom,essence)
        self.marchandise = marchandise

    def se_deplacer(self):
        print("je sure vole les airs")


v1= Vehicule("F22 Rapport", 2400)
v1.se_deplacer()
voiture1 = Voiture("toyota supra",90,420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")
av1 = Avion("F22 Raptor", 2400, "missiles")
av1.se_deplacer()#il va voir le premier se_deplacer et la prend


class ObjetJeu:
    pass
class Arme:
    pass
class Fusil(Arme,ObjetJeu):
    pass

class Animal:
    def __init__(self,nom):
        self.nom = nom
    def manger(self):
        print(self.nom,"mange...")

class Reptile(Animal):
    def __init__(self,nom,regime_alimentaire):
        Animal.__init__(self,nom)
        self.regime_alimentaire = regime_alimentaire

    def mange(self):
        print("le reptile mange...")

lezard = Reptile("Lezard","grenouille")
lezard.manger()
print(isinstance(lezard,Animal))#verifi si lezard est un objet de la classe animal
if isinstance(lezard,Animal):
    print("Lezard est un animal")
if issubclass(Reptile,Animal):
    print("reptile est une fille animal")





#     has = hashlib.md5()
#     has.update(resultat.encode('utf-8'))
#     hash_en_md5 = has.hexdigest()

# file_path = path.home().joinpath("dow")

#     encoded = b64encode(fichier_json)
# importing Image class from PIL package  



# from PIL import Image 
   
# creating a object  
# image = Image.open(r"C:\Users\System-Pc\Desktop\python.png") 
# MAX_SIZE = (100, 100) 
  
# image.thumbnail(MAX_SIZE) 
  
# creating thumbnail 
# image.save('pythonthumb.png') 
# image.show() 