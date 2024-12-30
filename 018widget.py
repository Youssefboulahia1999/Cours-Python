#coding:utf-8
import tkinter

app = tkinter.Tk()
app.geometry("400x300")
app.title("variable tkinter")

def hello():
    print("hello")

def show_about():
    about_window=tkinter.Toplevel(app)
    app.title("variable tkinter")
    

#widget LabelFrame
mainframe = tkinter.Frame(app,height=200,width="300",borderwidth=1)
label = tkinter.Label(app, text="boojours")
ent = tkinter.Entry(app)
btn = tkinter.Button(mainframe,text="bienvenue")

#widget menu
mainmenu = tkinter.Menu(app)
#menu
first_menu = tkinter.Menu(mainmenu,tearoff=0)
#valeur de menu
first_menu.add_command(label="option1", command=hello)
first_menu.add_command(label="option2")
first_menu.add_separator()
first_menu.add_command(label="quit",command=app.quit)

second_menu = tkinter.Menu(mainmenu,tearoff=0)

second_menu.add_command(label="commande1")
second_menu.add_command(label="a propos",command=show_about)

mainmenu.add_cascade(label="Premier",menu=first_menu)
mainmenu.add_cascade(label="second",menu=second_menu)

label.pack()
ent.pack()
btn.pack()
mainframe.pack()

app.config(menu=mainmenu)
app.mainloop()
