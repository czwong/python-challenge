import os

import csv

import re

txtpath = os.path.join('..', 'Resources', 'paragraph_3.txt')

with open(txtpath,'r') as txtfile:
    
    txtreader = txtfile.readline()

    word_count=0
    sentence_count=0
    word = []
    sentence = []
    print(repr(txtreader))
    for i in re.split("[,-.!?\s]",txtreader):
        word_count+=1
        # print(i)
        word.append(i)
    
    for i in re.split("([.!?]?<=) +",txtreader):
        sentence_count+=1
        sentence.append(i)

    letters=[]
    for i in word:
        letters.append(re.split("[,]",i))
    

    print(word_count)
    print(sentence_count)
    # print(sentence)


