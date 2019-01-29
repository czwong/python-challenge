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
        total_vote+=1

        if i[2] not in candidate:
            candidate.append(i[2])
        else:
            pass

    for i in candidate:
        candidate_won=0
        csvfile.seek(0)
        next(csvreader)
        for j in csvreader:
            if j[2]==i:
                candidate_won+=1
            else:
                pass

        candidate_total_vote.append(candidate_won)
        percent_vote.append(round((candidate_won/total_vote)*100,3))

    winner=candidate_total_vote.index(max(candidate_total_vote))

    print("\nElection Results\n-------------------------")
    print(f"Total Votes: {total_vote}\n-------------------------")
    for candidates in range(len(candidate)):
        print(f"{candidate[candidates]}: {percent_vote[candidates]}% ({candidate_total_vote[candidates]})")
    print(f"-------------------------\nWinner: {candidate[winner]}\n-------------------------")


poll=open("PyPoll.txt","w")

poll.write("Election Results\n-------------------------\n")
poll.write(f"Total Votes: {total_vote}\n-------------------------\n")
for candidates in range(len(candidate)):
    poll.write(f"{candidate[candidates]}: {percent_vote[candidates]}% ({candidate_total_vote[candidates]})\n")
poll.write(f"-------------------------\nWinner: {candidate[winner]}\n-------------------------")