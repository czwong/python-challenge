import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    first_row=next(csvreader)

    total_month=0
    total_amount=0
    greatest_increase=first_row
    greatest_decrease=first_row

    csvfile.seek(0)
    next(csvreader)

    for i in csvreader:
        total_month+=1
        total_amount+=int(i[1])

        if int(i[1])>int(greatest_increase[1]):
            greatest_increase=i
        
        elif int(i[1])<int(greatest_decrease[1]):
            greatest_decrease=i

        else:
            pass
    # max_index=greatest_increase.index(max(greatest_increase))
    # min_index=greatest_decrease.index(min(greatest_decrease))
    

    print("\nFinancial Analysis \n----------------------------")
    print(f"Total Month: {str(total_month)}")
    print(f"Total: ${str(total_amount)}")
    print(f"Greatest Increase in Profit: {greatest_increase[0]} ({greatest_increase[1]})")
    print(f"Greatest Decrease in Profit: {greatest_decrease[0]} ({greatest_decrease[1]})")

bank=open("PyBank.txt","w")

bank.write("Financial Analysis \n----------------------------")
bank.write(f"\nTotal Month: {str(total_month)}")
bank.write(f"\nTotal: ${str(total_amount)}")
bank.write(f"\nGreatest Increase in Profit: {greatest_increase[0]} ({greatest_increase[1]})")
bank.write(f"\nGreatest Decrease in Profit: {greatest_decrease[0]} ({greatest_decrease[1]})")