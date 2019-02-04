import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    total_vote=0
    county=[]
    candidate=[]
    candidate_total_vote=[]
    percent_vote=[]

    for i in csvreader:
        #Counts total votes
        total_vote+=1

        #Appends candidate names into empty list (cadidate)
        if i[2] not in candidate:
            candidate.append(i[2])
            candidate_total_vote.append(1)
        else:
            candidate_total_vote[candidate.index(i[2])]+=1

    print(candidate_total_vote)