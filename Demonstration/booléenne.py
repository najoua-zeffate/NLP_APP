#importaion des librairies nécaissires 
import pandas as pd
import spacy
from nltk.stem.snowball import SnowballStemmer
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk import word_tokenize
stemmer = SnowballStemmer(language='french')
#chargement du model français
nlp = spacy.load("fr_core_news_sm")
test="Bouygues a eu une coupure de réseau à  Marseille"
test1="Le réseau sera bientot rétabli à  Marseille"
#Récupération des mots vides
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
#récuperer la phrase 
test=" ".join(test)
test1=" ".join(test1)
t=test.split()
t1=test1.split()
total=set(t).union(set(t1))

#création de dictionnaire de mots et leur accurence pour chaque phrase
dic1=dict.fromkeys(total,0)
dic2=dict.fromkeys(total,0)

for word in t:
   dic1[word]+=1
    
for word in t1:
    dic2[word]+=1
#transformation des résultats sous format trames de donnÃ©es 
print(pd.DataFrame([dic1, dic2]))






