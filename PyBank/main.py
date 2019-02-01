import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    #This row will be used to find greatest_increase and greatest_decrease
    first_row=next(csvreader)

    total_month=0
    total_amount=0
    greatest_increase=first_row
    greatest_decrease=first_row
    profit_loss = []

    #Reads back to beginning of file
    csvfile.seek(0)

    #Skip header
    next(csvreader)

    for i in csvreader:
        total_month+=1
        total_amount+=int(i[1])

        #Append profit/loss column to empty list
        profit_loss.append(i[1])

        #Checks to see if next row is greater than current value
        if int(i[1])>int(greatest_increase[1]):
            
            #If true, greatest_increase equals to new row
            greatest_increase=i
        
        #Checks to see if next row is lower than current value
        elif int(i[1])<int(greatest_decrease[1]):

            #If true, greatest_decrease equals to new row
            greatest_decrease=i

        else:
            pass

    change=[]

    #Start at i=1, starting at second index of list
    for i in range(len(profit_loss))[1:]:
        change.append(int(profit_loss[i])-int(profit_loss[i-1]))

    average = 0
    
    for i in change:
        average+=i
    
    average = round(average/len(change),2)

    print("\nFinancial Analysis \n----------------------------")
    print(f"Total Month: {str(total_month)}")
    print(f"Total: ${str(total_amount)}")
    print(f"Average Change: ${str(average)}")
    print(f"Greatest Increase in Profit: {greatest_increase[0]} ({greatest_increase[1]})")
    print(f"Greatest Decrease in Profit: {greatest_decrease[0]} ({greatest_decrease[1]})")

bank=open("PyBank.txt","w")

bank.write("Financial Analysis \n----------------------------")
bank.write(f"\nTotal Month: {str(total_month)}")
bank.write(f"\nTotal: ${str(total_amount)}")
bank.write(f"\nAverage Change: ${str(average)}")
bank.write(f"\nGreatest Increase in Profit: {greatest_increase[0]} ({greatest_increase[1]})")
bank.write(f"\nGreatest Decrease in Profit: {greatest_decrease[0]} ({greatest_decrease[1]})")