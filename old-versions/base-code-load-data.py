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

# Jonathan Hernandez
def gender_feature_custom(name):
    return {'suffix1': name[-1:],
            'suffix2': name[-2:],
            'prefix1': name[0],
            'prefix2': name[0:2]}
            
featuresets = [(gender_feature_custom(n), g) for (n,g) in names]
test_set, dev_test_set, train_set = featuresets[:500], featuresets[500:1000], featuresets[1000:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
