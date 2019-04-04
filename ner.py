import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# exporting encoding utf-8 stuff because the file was being treating like a str but was a byte and some issue was happening and this solution worked, yay ~ thanks guy on stackoverflow
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#opening the file from the source and then reading it
#book = open("/Users/nanavati_sneha/Documents/2019 /coding projects/gutenberg-project-data/crime_and_punishment").read()

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])
pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])
