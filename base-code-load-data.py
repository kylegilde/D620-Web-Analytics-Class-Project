import pandas as pd
import nltk
from nltk.corpus import names
import random
#nltk.download('names') # first time only

# female names usually end in a,i,e and male names are k,o,r,s,t
#return the last letter in a word
def gender_features(word):
   return {'last_letter': word[-1]}

names = ([(name, 'male') for name in names.words('male.txt')] +
       [(name, 'female') for name in names.words('female.txt')])

random.seed(4)
random.shuffle(names)