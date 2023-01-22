
#importaion des librairies
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS 
from nltk.stem.snowball import SnowballStemmer
#Un des stemmers les plus connus est le Snowball Stemmer.Ce stemmer est disponible en français
stemmer = SnowballStemmer(language='french')
#phrase de test
test="Marchait marcherait marche marché "
#Récupération des mots vides
mots_vides=set(STOP_WORDS)
#converstion Majiscule/miniscule
test=test.lower()
#chargement du model français
nlp = spacy.load("fr_core_news_sm")
doc = nlp(test)
def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]
#Stemming 
Stemming=[]
for mots in return_stem(test):
    if mots not in mots_vides:
        Stemming.append(mots)
#nettoyage de la phrase des mots vides
Clean_MotsVides=[]
for word in Stemming:
    if word not in mots_vides:
        Clean_MotsVides.append(word)
#la nouvelle phrase devient
test=" ".join(Clean_MotsVides)
print(test)