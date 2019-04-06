
from bs4 import BeautifulSoup
import requests
import re
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load('en')


def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://www.nytimes.com/2019/04/04/us/politics/trump-biden.html')
article = nlp(ny_bb)

# // ner detection for the article
for ent in article.ents:
    print(ent.text, ent.label_)
