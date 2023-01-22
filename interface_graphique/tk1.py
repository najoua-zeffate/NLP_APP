# coding: utf-8
 
from tkinter import Tk
from tkinter import Label
from tkinter import Button,StringVar,Entry
from tkinter.filedialog import askopenfilename

fenetre = Tk()
fenetre.geometry("350x200")
fenetre.title("SimDoc")
x = StringVar(fenetre)
y = StringVar(fenetre)
Label(fenetre,text="Donner le chemin du premier fichier:").place(x=0,y=0)
entry = Entry(fenetre, textvariable=x)
entry.place(x=150,y=25)
Label(fenetre,text="Donner le chemin du deuxiéme fichier:").place(x=0,y=50)
entry1= Entry(fenetre, textvariable=y)
entry1.place(x=150,y=75)
def opeft():
       x.set(askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')]))
       
bouton = Button(fenetre, text="fichier1", command=opeft)
bouton.place(x=280,y=20)

def opeft1():
       y.set(askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')]))      
       
bouton1 = Button(fenetre, text="fichier2", command=opeft1)
bouton1.place(x=280,y=70)
bouton2 = Button(fenetre, text="Runtest", command=fenetre.quit)
bouton2.place(x=140,y=125)
fenetre.mainloop()


