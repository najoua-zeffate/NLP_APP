#importaion des librairies nécaissires 
import pandas as pd
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk import word_tokenize
#chargement du model français
nlp = spacy.load("fr_core_news_sm")
test="Bouygues a eu une coupure de réseau à Marseille"
test="""La nature est l'ensemble des êtres vivants, animaux et végétaux, ainsi que le milieu où ils se trouvent (minéraux, mers, montagnes, continents) qu'on trouve dans l'Univers.
En fait, la nature est tout ce qui n'est pas construit directement par l'homme, qui est appelé alors « artificiel ». 
La nature est souvent associée à l'environnement, la forêt, ou les rivières.
C'est aussi le monde physique qui nous entoure."""
test1="Le réseau sera bientot rétabli à Marseille"
test2="""L'Univers est l'ensemble de tout ce qui existe, régi par un certain nombre de lois.

La cosmologie cherche à appréhender l'Univers d'un point de vue scientifique, comme l'ensemble de la matière distribuée dans l'espace-temps. 
Pour sa part, la cosmogonie vise à établir une théorie de la création de l'Univers sur des bases philosophiques ou religieuses. 
La différence entre ces deux définitions n'empêche pas nombre de physiciens d'avoir une conception finaliste de l'Univers (voir à ce sujet le principe anthropique).

Si l'on veut faire correspondre le mouvement des galaxies avec les lois physiques telles qu'on les conçoit actuellement,
 on peut considérer que l'on n'accède par l'expérience qu'à une faible partie de la matière de l'Univers1, 
le reste se composant de matière noire. 
Par ailleurs, pour expliquer l'accélération de l'expansion de l'Univers, il faut également introduire le concept d'énergie sombre. 
Plusieurs modèles alternatifs ont été proposés pour faire correspondre les équations et nos observations en prenant d'autres approches."""
test="aa bb cc"
test1="aa ee ff"
#Récupération des mots vides
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
#récuperer la phrase 
test=" ".join(test)
test1=" ".join(test1)
t=test.split()
t1=test1.split()
total=set(t).union(set(t1))
print(total)
#créaation de dictionnaire de mots et leur accurence pour chaque phrase
dic1=dict.fromkeys(total,0)
dic2=dict.fromkeys(total,0)
for word in t:
    dic1[word]+=1
    
for word in t1:
    dic2[word]+=1
#transformation des résultats sous format trames de donnÃ©es 
print(pd.DataFrame([dic1, dic2]))
#TF méthode
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
#exécuter nos phrases à travers la fonction tf
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