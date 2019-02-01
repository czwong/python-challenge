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
        else:
            pass

    for i in candidate:
        candidate_won=0

        #Seeks back to beginning of file to read
        csvfile.seek(0)

        #Skip header
        next(csvreader)

        for j in csvreader:

            #If candidate name matches name in cadidate list increase their vote count
            if j[2]==i:
                candidate_won+=1
            else:
                pass

        #Appends each candidate vote count to empty list candidate_total_vote
        candidate_total_vote.append(candidate_won)
        percent_vote.append(round((candidate_won/total_vote)*100,3))

    #Identitfy winner by matching the highest score in list candidate_total_vote
    winner=candidate_total_vote.index(max(candidate_total_vote))

    print("\nElection Results\n-------------------------")
    print(f"Total Votes: {total_vote}\n-------------------------")
    for candidates in range(len(candidate)):
        print(f"{candidate[candidates]}: {percent_vote[candidates]}% ({candidate_total_vote[candidates]})")
    print(f"-------------------------\nWinner: {candidate[winner]}\n-------------------------")

#Write results to txt file
poll=open("PyPoll.txt","w")

poll.write("Election Results\n-------------------------\n")
poll.write(f"Total Votes: {total_vote}\n-------------------------\n")
for candidates in range(len(candidate)):
    poll.write(f"{candidate[candidates]}: {percent_vote[candidates]}% ({candidate_total_vote[candidates]})\n")
poll.write(f"-------------------------\nWinner: {candidate[winner]}\n-------------------------")