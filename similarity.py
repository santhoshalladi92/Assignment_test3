__author__ = 'SANTHOSH'

import enchant
import math
import nltk
from stemming.porter2 import stem
from nltk.corpus import stopwords

porter = nltk.PorterStemmer()
dictionary = enchant.Dict("en_US")


def cosinesimilarity(data1, data2):
    dot = 0
    vecA = 0
    vecB = 0
    for token in data1.keys():
        if data2.has_key(token):
            dot = dot + data1[token] * data2[token]
    for token in data1.keys():
        vecA = vecA + data1[token] * data1[token]
    for token in data2.keys():
        vecB = vecB + data2[token] * data2[token]
    modA = math.sqrt(vecA)
    modB = math.sqrt(vecB)
    print (dot) / (modA * modB)
    pass


def main():
    stop = set(stopwords.words('english'))
    tokens1 = []
    with open("set_1.txt", "r") as f1:
        for line in f1:
            tokens1 = tokens1 + [i for i in line.split() if i not in stop]
    tokens2 = []
    with open("set_2.txt", "r") as f2:
        for line in f2:
            tokens2 = tokens2 + [i for i in line.split() if i not in stop]

    data1 = {}
    true = {}
    false = {}
# implementing spell check
    
    for x in tokens1:
        if dictionary.check(x):
            if x in true:
                true[x] += 1
            else:
                true[x] = 1
        else:
            if x in false:
                false[x] += 1
            else:
                false[x] = 1

    for x in false:
        templist = dictionary.suggest(x)
        for y in templist:
            if y in true:
                true[y] = true[y] + false[x]
                false[x] = 0
                break

    for x in false:
        if false[x] != 0:
            true[x] = false[x]

     
#stemming and storing as key value pairs in data1 for file set_1
    for x in true:
        modified = stem(x)
        if modified not in data1:
            data1[modified] = true[x]
        else:
            data1[modified] = data1[modified] + true[x]

    data2 = {}
    true = {}
    false ={}
# implementing spell check
    for x in tokens2:
        if dictionary.check(x):
            if x in true:
                true[x] += 1
            else:
                true[x] = 1
        else:
            if x in false:
                false[x] += 1
            else:
                false[x] = 1

    for x in false:
        templist = dictionary.suggest(x)
        for y in templist:
            if y in true:
                true[y] = true[y] + false[x]
                false[x] = 0
                break

    for x in false:
        if false[x] != 0:
            true[x] = false[x]
#stemming and storing as key value pairs in data2 for file set_2
    for x in true:
        modified = stem(x)
        if modified not in data2:
            data2[modified] = true[x]
        else:
            data2[modified] = data2[modified] + true[x]


    cosinesimilarity(data1, data2)


if __name__ == "__main__":
    main()
