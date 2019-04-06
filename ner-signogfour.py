# coding: utf8

import spacy
nlp = spacy.load('en')
from spacy import displacy

# // opening a text and reading it. using the enc thingy here because it was throwing attribution errors
book = unicode(open("/Users/nanavati_sneha/Documents/2019 /coding projects/gutenberg-project-data/sign_of_four.txt").read().decode('utf8'))
doc = nlp(book)

# //tokenization(?) me thinks ...
for word in list(doc.sents):
    print word, word.tag_

# // sentence detection and separation
for sent in doc.sents:
    # print(sent)

# // performing POS tagging using spacy
print([(token.text, token.tag_) for token in doc])

# // entity recognision from the doc
for ent in doc.ents:
    print(ent.text, ent.label_)

# // displaying it all pretty but doesn't work on terminal, needs jupyter (doesn't work as of now, buggy)
display the ner using spacy's displacy
displacy.render(doc, style='ent', jupyter=True)


#  //chunking noun phrases and even mentioning the root of the phrase
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.label_, chunk.root.text)
