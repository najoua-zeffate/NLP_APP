#importaion des librairies n�caissires 
import pandas as pd
import spacy
from nltk.stem.snowball import SnowballStemmer
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk import word_tokenize
stemmer = SnowballStemmer(language='french')
#chargement du model fran�ais
nlp = spacy.load("fr_core_news_sm")
test="Bouygues a eu une coupure de r�seau � Marseille"
test1="Le r�seau sera bientot r�tabli � Marseille"
#R�cup�ration des mots vides
mots_vides=set(STOP_WORDS)
test=test.lower()
test1=test1.lower()
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

#cr�ation de dictionnaire de mots et leur accurence pour chaque phrase
dic1=dict.fromkeys(total,0)
dic2=dict.fromkeys(total,0)

for word in t:
   dic1[word]+=1
    
for word in t1:
    dic2[word]+=1
#transformation des r�sultats sous format trames de données 
print(pd.DataFrame([dic1, dic2]))






