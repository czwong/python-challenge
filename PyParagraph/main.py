import os

import csv

import re

txtpath = os.path.join('..', 'Resources', 'paragraph_3.txt')

with open(txtpath,'r') as txtfile:
    
    txtreader = txtfile.readline()

    word_count=0
    sentence_count=0

    for i in txtreader.split(' '):
        print(i)
        word_count+=1
    
    for i in re.split("[.!?]\s",txtreader):
        sentence_count+=1

    for i in re.split("[\s,.!?]\s",txtreader):
        print(i)
    print(word_count)
    print(sentence_count)


