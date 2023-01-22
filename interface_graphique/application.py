from tkinter import Tk
from tkinter import Label
from tkinter.ttk import Progressbar
from tkinter import ttk
from tk1  import x
from tk1 import  y
import spacy 
from spacy.lang.fr.stop_words import STOP_WORDS 
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from nltk import word_tokenize
x2=x
x1=y
with open(x2.get(),"r",encoding="utf-8") as f:
    test=f.read()
with open(x1.get(),"r",encoding="utf-8") as f1:
    test1=f1.read()
#converstion Majuscule/minuscule
test1=test1.lower()
test=test.lower()
#chargement du model français
nlp = spacy.load("fr_core_news_sm")
doc=nlp(test)
doc1=nlp(test1)
#Récupération des mots vides
par={"(",")",".",",",";",":","!","?",'""',"''","#","'","«","»","[","]","{","}","/","^","-","_"}
fr_stop=set(STOP_WORDS)
fr_stop=fr_stop.union(par)
fr_stop.add("@")
#lemmatisation
lem=[]
for word in doc:
         lem.append(word.lemma_)
lem1=[]
for word in doc1:
         lem1.append(word.lemma_)
clean=[]
for word in lem:
    if word not in fr_stop:
        clean.append(word)
clean1=[]
for word in lem1:
    if word not in fr_stop:
        clean1.append(word)
test=" ".join(clean)
test1=" ".join(clean1)
#tokenization
R=word_tokenize(test)
R1=word_tokenize(test1)
str0=" ".join(R)
str1=" ".join(R1)
#Union des deux documents
t=str0.split()
t1=str1.split()
total=set(t).union(set(t1))
#création de dictionnaire de mots et leur accurence pour chaque phrase
dic1=dict.fromkeys(total,0)
dic2=dict.fromkeys(total,0)

for word in t:
   dic1[word]+=1
    
for word in t1:
    dic2[word]+=1
#transformation des résultats sous format trames de donnÃ©es 
#print(pd.DataFrame([dic1, dic2]))
#Calcul de la similarité
x=np.array(pd.Series(dic1))
y=np.array(pd.Series(dic2))
cos_sim =(dot(x,y)/(norm(x)*norm(y)))*100
if cos_sim>=100:
    cos_sim=100
#print("%.2f" % cos_sim,'%')
#Création d'une barre de progression pour l'affichage du résultat avec TKinter
fenetre=Tk()
fenetre.title("Résultat")
fenetre.geometry("350x200")
style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='green')
bar=Progressbar(fenetre,length=200,style="black.Horizontal.TProgressbar")
bar['value']=cos_sim 
Label(fenetre,text="La pourcentage de similarité entre  les deux documents est: ").place(x=15,y=70)
Label(fenetre,text=(int(cos_sim),"%")).place(x=160,y=125)
bar.place(x=70,y=100)

fenetre.mainloop()

