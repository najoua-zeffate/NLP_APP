#importaion des librairies
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk import word_tokenize
#chargement du model français
nlp = spacy.load("fr_core_news_sm")
#phrase de test
test="Bouygues a eu une coupure de réseau à Marseille "
#Récupération des mots vides
mots_vides=set(STOP_WORDS)
#converstion Majuscule/minuscule
test=test.lower()
doc = nlp(test)
#Lemmatisation
lemmatisation=[]
for mots in doc:
        lemmatisation.append(mots.lemma_)
#nettoyage de la phrase des mots vides
Clean_MotsVides=[]
for word in lemmatisation:
    if word not in mots_vides:
        Clean_MotsVides.append(word)
#la nouvelle phrase devient
test=" ".join(Clean_MotsVides)
print(test)
#tokenisation
test=word_tokenize(test)
print(test)
