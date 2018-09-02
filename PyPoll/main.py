'''
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
'''
import os
import csv

total_votes=[]
vote_result = {}
result = []
source_csv = os.path.join("election_data.csv")
with open(source_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        total_votes.append(row[0])
        if row[2] not in vote_result.keys():
            vote_result[row[2]] = 1
        else:
            vote_result[row[2]] = int(vote_result[row[2]]) +1

result.append(f'Election Results')
result.append(f'------------------------------------------------------')
result.append(f'Total Votes:   {len(total_votes)}')
result.append(f'------------------------------------------------------')

for candidate in vote_result.keys():
    percent = "{:.2%}".format((vote_result[candidate])/(len(total_votes)))
    result.append(f'{candidate} : {percent} ({vote_result[candidate]})')

result.append(f'------------------------------------------------------')
result.append(f'Winner: {max(vote_result.keys(), key=(lambda k: vote_result[k]))}')
result.append(f'------------------------------------------------------')
[print(x) for x in result]
with open('output.csv', mode='w', newline='') as summary:
    summary_writer = csv.writer(summary, delimiter=',')
    [summary_writer.writerow([x]) for x in result]