# -*- coding: utf-8 -*-

import pandas as pd
from pandas import *
from scipy import spatial
import operator
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

import math
from textblob import TextBlob as tb

## part of the code from http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def f(x):
     return Series(dict(asin = x['asin'],
                        Text = "{%s}" % ', '.join(str(ele) for ele in x['reviewText']), 
                        rating = x["overall"].mean()))

#read data from csv
def readcsv(path):
    return pd.read_csv(path, iterator=True, chunksize=10000, skip_blank_lines=True)

#normalize cosine distance item-item

tp = readcsv("Content500k.csv") 
df = concat(tp, ignore_index=True)

#delete item which has less number of ratings than 500
df = df.groupby("asin").filter(lambda x: len(x) > 500)
df = df.groupby("asin").apply(f)
#df = df.drop(df.columns[[0]], axis=1)

bloblist =[]

outfile = open('tfidf.txt', 'w')
for i in xrange(len(df)):
    avg_str = '\t'.join([str(df.index[i]), 'rating(avg)', str(df.ix[i,1])])
    avg_str = avg_str + '\n'
    outfile.write(avg_str)
    bloblist.append(tb(df.ix[i,0].lower()))

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)  
    for word, score in sorted_words[:5]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        item_str = '\t'.join([str(df.index[i]), word, str(1)])
        item_str = item_str + '\n'
        outfile.write(item_str)

outfile.close()


