#coding:utf-8
import tkinter

"""
StringVar()
IntVar()
DoubleVar() float
BooleanVar() boolean
"""
#observateur change le modifie en la nouvelle valeur du label
def update_label(*args):
    var_label.set(var_entry.get())

app = tkinter.Tk()
app.geometry("400x300")
app.title("variable tkinter")

var_entry = tkinter.StringVar()
var_entry.trace("w",update_label)
entry = tkinter.Entry(app,textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, text="bonjour",textvariable=var_label)
var_label.set("la label...")



entry.pack()
label.pack()
app.mainloop()
