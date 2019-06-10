import numpy as np
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from matplotlib import pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import wordcloud
import gensim
from os import path
from PIL import Image

#import gensim packages
from gensim import corpora, models, similarities
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#import factiva data
factiva = open("Factiva-20181112-1726.txt",'r')
uav=factiva.read()

#remove punctuation

#make all words lowercase
tokens = [w for w in word_tokenize(uav.lower()) if w.isalpha()]
#get rid of stop words
no_stops = [t for t in tokens if t not in stopwords.words('english')]
#lemmatize words
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
#count most common
uav_counter = Counter(lemmatized)
print(uav_counter.most_common(10))

#create and generate a Wordcloud image
wordcloud = WordCloud().generate(uav)

#display the generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
