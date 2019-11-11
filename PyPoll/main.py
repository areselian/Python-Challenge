# The total number of votes cast
# A complete list of candidates who received votes 
# The percentage of votes each candidate won (votes per candidate/total votes)
# The total number of votes each candidate won 
# The winner of the election based on popular vote

import os
import csv

election_data = os.path.join("Resources", "election_data.csv")


total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
candidates_list = []

with open(election_data, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes = total_votes + 1

        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1
        if row[2] in candidates_list:
            continue
        else:
            candidates_list.append(row[2])

    # Percent of each candidate (their individual code / total votes)
    khan_percent = (khan_votes) / (total_votes)
    khan_percent = "{:.3%}".format(khan_percent)
    correy_percent = (correy_votes) / (total_votes)
    correy_percent = "{:.3%}".format(correy_percent)
    li_percent = (li_votes) / (total_votes)
    li_percent = "{:.3%}".format(li_percent)
    otooley_percent = (otooley_votes) / (total_votes)
    otooley_percent = "{:.3%}".format(otooley_percent)

    max_votes = max([khan_votes, correy_votes, li_votes, otooley_votes])

    if max_votes == khan_votes:
        winner = "Khan"
    elif max_votes == correy_votes:
        winner = "Correy"
    elif max_votes == li_votes:
        winner = "Li"
    else:
        winner = "O'Tooley"

    print(f"Election Results")
    print("----------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------")
    print(f"Khan: {khan_percent} ({khan_votes})")
    print(f"Correy:{correy_percent} ({correy_votes})")
    print(f"Li: {li_percent} ({li_votes})")
    print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
    print("----------------------")
    print(f"Winner: {winner} ")
    print("----------------------")

election_results = os.path.join("Analysis", "election_data.txt")

with open(election_results,  'w') as txtfile:
    txtfile.write(f"Election Results \n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"Khan: {khan_percent} ({khan_votes})\n")
    txtfile.write(f"Correy:{correy_percent} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent} ({otooley_votes})\n")
    txtfile.write(f"Winner: {winner}\n")




