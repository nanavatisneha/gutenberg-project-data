# coding: utf8

import spacy
nlp = spacy.load('en')
from spacy import displacy

# // opening a text and reading it. using the enc thingy here because it was throwing attribution errors
book = unicode(open("/Users/nanavati_sneha/Documents/2019 /coding projects/gutenberg-project-data/sign_of_four.txt").read().decode('utf8'))
doc = nlp(book)

# // sentence detection and separation
for sent in doc.sents:
    print(sent)
