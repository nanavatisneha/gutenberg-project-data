# // what's going on: in this project we try to do i) word tokenization, ii) sentence tokenization and iii) POS tagging iv) frequency distribution, v) wordcloud
# author: nanavati_sneha


import nltk
#using nltk for word tokenization
from nltk import word_tokenize
#using nltk for sentence tokenization
from nltk import sent_tokenize
# for pos tagging
from nltk import pos_tag

#to use the wordcloud thingy
from wordcloud import WordCloud, STOPWORDS

#matplotlib and its necessary dipendencies, this threw up some erros but resolved it
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# exporting encoding utf-8 stuff because the file was being treating like a str but was a byte and some issue was happening and this solution worked, yay ~ thanks guy on stackoverflow
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# // in continutation of part one: getting data now we are playing around with the text of crime and punishment //

# // part two: word tokenization //

#opening the file from the source and then reading it
book = open("/Users/nanavati_sneha/Documents/2019 /coding projects/gutenberg text/crime_and_punishment").read()
#sending the file to word tokenizer and tokenzing it
word_tokens = word_tokenize(book)
#printing the results
# print word_tokens
#finding the number of word tokens in the document
num_words = len(word_tokens)
#and printing the number of words
# print("Number of words:", num_words)

# // part three: sentence tokenization //

# tokenising sentences and printing them
sent_tokens = sent_tokenize(book)
# print(sent_tokens)
# finding the number of sentences and printing them
num_sents = len(sent_tokens)
# print("Number of sentences:", num_sents)

# //part four: POS tagging //

#using the word tonizer from part one and performing a part-of-speech tagging
tagged_tokens = pos_tag(word_tokens)
#printing the tokens with wrt part of speech
# print('Tokens tagged with part of speech:', tagged_tokens)

# //part five: frequency distribution plot matplotlib //

fd = nltk.FreqDist(word_tokens)
fd.plot(5,cumulative=False)

# //part five: word cloud //
#creating a word cloud
wordcloud = WordCloud(max_font_size=60).generate(book)
plt.figure(figsize=(16,12))
# plot wordcloud in matplotlib
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()











# ---------------------------------------------------------------------------
# random notes: one can also use the following invocation in beginning to use their own corpora (in this case crime and punishment)
#from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/usr/share/dict'
# ~ yet another way to open and read a filesf = open("file.txt", "r")
    # inputfile = f.read()
