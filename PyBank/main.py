'''
Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

'''
import os
import csv

source_csv = os.path.join("budget_data.csv")

months=[]
gain_loss = []
changes= []
sum = 0
change = 0
total_change = 0
result=[]
# Open and read csv
with open(source_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        months.append(row[0])
        gain_loss.append(row[1])
        sum = sum + int(row[1])
    for i in range(0,len(gain_loss)-1) :
        change = float(gain_loss[i+1]) - float(gain_loss[i]) 
        changes.append(change)
        total_change = total_change + change
   #index needs +1 as the way "change" was calculated is 1 off.
    max_month = changes.index(max(changes)) +1
    min_month = changes.index(min(changes)) +1
    
    result.append(f'Financial Analysis')
    result.append(f'------------------------------------------------------')
    result.append(f'Total Months:   {len(set(months))}')
    result.append(f'Total: ${sum}')
    result.append(f'Average  Change: ${total_change/(len(gain_loss)-1)}')
    result.append(f'Greatest Increase in Profits: {months[max_month]} (${max(changes)})')
    result.append(f'Greatest Decrease in Profits: {months[min_month]} (${min(changes)})')

[print(x) for x in result]

    
with open('output.csv', mode='w', newline='') as summary:
    summary_writer = csv.writer(summary, delimiter=',')
    [summary_writer.writerow([x]) for x in result]
