# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:23:33 2018

@author: Nero
"""

import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
"""
      Welcome to WORD JUMBLE!!!

      Unscramble the leters to make a word.
      (press the enter key at prompt to quit)
      """
      )
print("The jumble is:", jumble)
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it, you guessed it!\n")
print("Thanks for playing")

input("\n\nPress the enter key to exit")


from sklearn.feature_extraction.text import TfidVectorizer
import pandas as pd
texts =["good movie","nota good movie","did not like",
        "i like it","good one"
         ]

tfidf=TfidVectorizer(min_df=2,max_df=0.5,ngram_range=(1,2))
features=tfidf.fit_transform(texts)
pd.DataFrame(features.todense(),
             columns=tfidf.get_feature_names()
             )

import nltk
import sklearn

print('The nltk version is {}.'.format(nltk.__version__))
print('The scikit-learn version is {}.'.format(sklearn.__version__))
