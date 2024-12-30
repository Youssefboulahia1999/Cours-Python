#coding:utf-8
import tkinter
#from tkinter import *

#import d'une fonction
from tkinter import messagebox

"""
showerror
showinfo
showwarniing
askquestion
askokcancel
askyesno
askretrycancel
"""
def show_modale_window():
    messagebox.showerror("ERREUR","un probleme est survenu")

#ouvre tkinter
mainapp = tkinter.Tk()

btn = tkinter.Button(mainapp,text="declencher une erreur", command=show_modale_window)

mainapp.title("mon premier programme")
#mainapp.minsize(640,480)
#mainapp.maxsize(1200,800)
#mainapp.geometry("800x600")
#mainapp.postionfrom("user")
#mainapp.sizefrom("user")
mainapp.geometry("800x600+50+100")

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 800
window_y = 600
posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x,window_y,posX,posY)


#pour interdire le redimentionement 
#mainapp.resizable(width=False, height=False)

#ecrie un label
label_welcome = tkinter.Label(mainapp,text=" bienvenue a tous !")
#donne une input
entry_name = tkinter.Entry(mainapp)
#donne une input prive
entry_name = tkinter.Entry(mainapp, show="*")
#chekebox optionel 
check_widget = tkinter.Checkbutton(mainapp, text="Publier ?",offvalue=2,onvalue=5,height=15,width=18)

#input radio
radio_widget = tkinter.Radiobutton(mainapp,text="Homme",value=1)
radio_widget2 = tkinter.Radiobutton(mainapp,text="Femme",value=0)

#input jauge de 10 a 100 interval en 25
scale_w = tkinter.Scale(mainapp,from_=0, to=250, tickinterval=25)
#input valeur chiffre
spin_w = tkinter.Spinbox(mainapp,from_=1,to=10)

lb = tkinter.Listbox(mainapp)
lb.insert(1,"windows")
lb.insert(2,"linux")
lb.insert(3,"macOs")


def hello():
    print("bonjours terminal")

button_quit = tkinter.Button(mainapp,text="ok",width="25",command=hello)

#pack est une methode qui donne un espace 
btn.pack()
lb.pack()
spin_w.pack()
scale_w.pack()
radio_widget.pack()
radio_widget2.pack()
check_widget.pack()
button_quit.pack()
entry_name.pack()
label_welcome.pack()
#faire une boucle qui tourne jusqu'a la fin de l'utilisation
mainapp.mainloop()