import os

import csv

import re

txtpath = os.path.join('..', 'Resources', 'paragraph_3.txt')

with open(txtpath,'r') as txtfile:
    
    txtreader = txtfile.readline()

    word_count=0
    sentence_count=0
    letter_count=0
    word = []
    sentence = []

    for sentences in re.split("(?<=[.!?]) +",txtreader):
        sentence_count+=1
        sentence.append(sentences)

        for words in re.findall("[\w']+",sentences):
            word_count+=1
            word.append(words)
            
            for letters in re.findall(".",words):
                # print(letters)
                letter_count+=1

    sentence_avg = round(word_count/sentence_count,2)

    print("\nParagraph Analysis\n-----------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Sentence Length: {sentence_avg}")
    # print(word_count/len(word))

para = open("PyParagraph.txt","w")
para.write("Paragraph Analysis\n-----------------\n")
para.write(f"Approximate Word Count: {word_count}\n")
para.write(f"Approximate Sentence Count: {sentence_count}\n")
para.write(f"Average Sentence Length: {sentence_avg}")