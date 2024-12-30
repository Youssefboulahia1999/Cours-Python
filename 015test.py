#coding:utf-8

import pickle

class Player:
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def whoami(self):
        print("{} ({})".format(self.name,self.level))

p1=Player("youssef",10)

#enregistrement d'un objet dans un autre fichier
with open("Player.data","wb") as fic:
    #utilisation du module pickler fic designe ce ficher 
    record = pickle.Pickler(fic)
    #copie de l'objet p1
    record.dump(p1)

#recuper la sauvegarde de l'objet dans le fichier
with open("Player.data","rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoami()