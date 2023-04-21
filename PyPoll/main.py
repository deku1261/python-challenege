import os
import csv

candidates = {}
votes_per_candidate = []
break_line = "------------------------------"


file = '/Users/threshmain/Desktop/UPenn_pythonchallenge/python-challenge/PyPoll/Resources/election_data.csv'

openfile = open(file)

csvreader = csv.reader(openfile)
next(csvreader)
totalvotes = 0

for row in csvreader:
    totalvotes += 1
    name = row[2]
    if name in candidates:
        candidates[name] += 1
    else:
        candidates[name] = 1

     
candidates["Charles Casper Stockham Percent"] = round((candidates["Charles Casper Stockham"]/totalvotes) * 100, 2)
candidates["Diana DeGette Percent"] = round((candidates["Diana DeGette"]/totalvotes) * 100, 2)
candidates["Raymon Anthony Doane Percent"] = round((candidates["Raymon Anthony Doane"]/totalvotes) * 100, 2)


cand_winner = max(candidates, key=candidates.get)

print("Election Results")
print(break_line)
print("Total Vote: " + str(totalvotes))
print(break_line)
print("Charles Casper Stockham: " + str(candidates["Charles Casper Stockham Percent"]) + "%" + "(" + str(candidates["Charles Casper Stockham"]) + ")") 
print("Diana DeGette: " + str(candidates["Diana DeGette Percent"]) + "% " + "(" + str(candidates["Diana DeGette"]) + ")")
print("Raymon Anthony Doane: " + str(candidates["Raymon Anthony Doane Percent"]) + "% " + "(" + str(candidates["Raymon Anthony Doane"]) + ")")
print(break_line)
print("Winner: " + str(cand_winner))
print(break_line)

