#importaion des librairies nécessaires 
import spacy 
import fr_core_news_md
from spacy.lang.fr.stop_words import STOP_WORDS 
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from nltk import word_tokenize
#chargement du model français
#nlp=fr_core_news_md.load()
nlp = spacy.load("fr_core_news_sm")
x=input("Donner le chemin du premier fichier: ")
x1=input("Donner le chemin du deuxième fichier:")
with open(x,"r",encoding="utf-8") as f:
    test=f.read()
with open(x1,"r",encoding="utf-8") as f1:
    test1=f1.read()
#Transformer les deux doc en minuscule
test1=test1.lower()
test=test.lower()
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
#nettoyage 
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
#création des dictionnaires
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
#transformation des résultats sous format trames de données 
print(pd.DataFrame([dic1, dic2]))
#Calcul de la similarité
x=np.array(pd.Series(dic1))
y=np.array(pd.Series(dic2))
cos_sim =(dot(x,y)/(norm(x)*norm(y)))*100
#cos_sim=norm(x-y)*100
if cos_sim>=100:
    cos_sim=100
print("%.2f" % cos_sim,'%')


    

