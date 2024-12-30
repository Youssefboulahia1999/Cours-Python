#coding:utf-8


def parler (personnage, message):
    print("{} : {}" .format(personnage,message))

def au_revoir():
    print("au revoir")

""" si la valeur de name = a main """
if __name__ == "__main__":
    parler("jason","bonjour tout le monde")
    au_revoir()
