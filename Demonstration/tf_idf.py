#importaion des librairies n�caissires 
import pandas as pd
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk import word_tokenize
#chargement du model fran�ais
nlp = spacy.load("fr_core_news_sm")
test="Bouygues a eu une coupure de r�seau � Marseille"
test="""La nature est l'ensemble des �tres vivants, animaux et v�g�taux, ainsi que le milieu o� ils se trouvent (min�raux, mers, montagnes, continents) qu'on trouve dans l'Univers.
En fait, la nature est tout ce qui n'est pas construit directement par l'homme, qui est appel� alors � artificiel �. 
La nature est souvent associ�e � l'environnement, la for�t, ou les rivi�res.
C'est aussi le monde physique qui nous entoure."""
test1="Le r�seau sera bientot r�tabli � Marseille"
test2="""L'Univers est l'ensemble de tout ce qui existe, r�gi par un certain nombre de lois.

La cosmologie cherche � appr�hender l'Univers d'un point de vue scientifique, comme l'ensemble de la mati�re distribu�e dans l'espace-temps. 
Pour sa part, la cosmogonie vise � �tablir une th�orie de la cr�ation de l'Univers sur des bases philosophiques ou religieuses. 
La diff�rence entre ces deux d�finitions n'emp�che pas nombre de physiciens d'avoir une conception finaliste de l'Univers (voir � ce sujet le principe anthropique).

Si l'on veut faire correspondre le mouvement des galaxies avec les lois physiques telles qu'on les con�oit actuellement,
 on peut consid�rer que l'on n'acc�de par l'exp�rience qu'� une faible partie de la mati�re de l'Univers1, 
le reste se composant de mati�re noire. 
Par ailleurs, pour expliquer l'acc�l�ration de l'expansion de l'Univers, il faut �galement introduire le concept d'�nergie sombre. 
Plusieurs mod�les alternatifs ont �t� propos�s pour faire correspondre les �quations et nos observations en prenant d'autres approches."""
test="aa bb cc"
test1="aa ee ff"
#R�cup�ration des mots vides
mots_vides=set(STOP_WORDS)
doc=nlp(test)
doc1=nlp(test1)
#Lemmatisation
#Lemmatisation
lemmatisation=[]
for mots in doc:
        lemmatisation.append(mots.lemma_)
lemmatisation1=[]
for mots in doc1:
        lemmatisation1.append(mots.lemma_)
#nettoyage de la phrase des mots vides
Clean_MotsVides=[]
for word in lemmatisation:
    if word not in mots_vides:
        Clean_MotsVides.append(word)
Clean_MotsVides1=[]
for word in lemmatisation1:
    if word not in mots_vides:
        Clean_MotsVides1.append(word)
#la nouvelle phrase devient
test=" ".join(Clean_MotsVides)
test1=" ".join(Clean_MotsVides1)
#tokenisation
test=word_tokenize(test)
test1=word_tokenize(test1)
#r�cuperer la phrase 
test=" ".join(test)
test1=" ".join(test1)
t=test.split()
t1=test1.split()
total=set(t).union(set(t1))
print(total)
#cr�aation de dictionnaire de mots et leur accurence pour chaque phrase
dic1=dict.fromkeys(total,0)
dic2=dict.fromkeys(total,0)
for word in t:
    dic1[word]+=1
    
for word in t1:
    dic2[word]+=1
#transformation des r�sultats sous format trames de données 
print(pd.DataFrame([dic1, dic2]))
#TF m�thode
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
#ex�cuter nos phrases � travers la fonction tf
tfFirst = computeTF(dic1, t)
tfSecond = computeTF(dic2, t1)
#Converting to dataframe for visualization
print(pd.DataFrame([tfFirst, tfSecond]))
#idf 
def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict
idfs= computeIDF([dic1, dic2])
#print(idfs)
#tf_idf
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf
tfidfA = computeTFIDF(tfFirst, idfs)
tfidfB = computeTFIDF(tfSecond, idfs)
print(pd.DataFrame([tfidfA, tfidfB]))
x=np.array(pd.Series(tfidfA))
y=np.array(pd.Series(tfidfB))
cos_sim =(dot(x,y)/(norm(x)*norm(y)))*100
if cos_sim>=100:
    cos_sim=100
#print("%.2f" % cos_sim,'%')
#euclidienne
sim_eucl=norm(x-y)*100
if sim_eucl>=100:
    sim_eucl=100
print("%.2f" % sim_eucl,'%')