# Import modules
import os
import csv

# Set initial variables
vote_count = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Lists to store data
candidates = []


# Set path of file to read
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')

# Open budget_data.csv and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row in the .csv
    csv_header = next(csvreader)  

    #For each row in the .csv file starting from the second row
    for row in csvreader:
        # Count Months
        vote_count += 1

        # Create a list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        # Count number of votes for each candidate
        if row[2] == 'Khan':
            khan_votes += 1
        if row[2] == 'Correy':
            correy_votes += 1
        if row[2] == 'Li':
            li_votes += 1
        if row[2] == "O'Tooley":
            otooley_votes += 1

# Calculate percentage of votes for each candidate
khan_percentage = khan_votes / vote_count
correy_percentage = correy_votes / vote_count
li_percentage = li_votes / vote_count
otooley_percentage = otooley_votes / vote_count

# Format percentage to % with 3 decimal places
khan_percentage = ("{:.3%}".format(khan_percentage))
correy_percentage = ("{:.3%}".format(correy_percentage))
li_percentage = ("{:.3%}".format(li_percentage))
otooley_percentage = ("{:.3%}".format(otooley_percentage))

# Find what the most amount of votes were and find who the winner of the election is
winner = max(khan_votes, correy_votes, li_votes, otooley_votes)
if winner == khan_votes:
    winner = 'Khan'
elif winner == correy_votes:
    winner = 'Correy'
elif winner == li_votes:
    winner = 'Li'
elif winner == otooley_votes:
    winner = "O'Tooley"

# Print election results in terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
print(f"Khan: {khan_percentage} ({khan_votes})")
print(f"Correy: {correy_percentage} ({correy_votes})")
print(f"Li: {li_percentage} ({li_votes})")
print(f"O'Tooley: {otooley_percentage} ({otooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create .txt file with election results in Analysis folder
with open (os.path.join(dirname, 'Analysis', 'election_results.txt'), 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {vote_count}\n")
    file.write("-------------------------\n")
    file.write(f"Khan: {khan_percentage} ({khan_votes})\n")
    file.write(f"Correy: {correy_percentage} ({correy_votes})\n")
    file.write(f"Li: {li_percentage} ({li_votes})\n")
    file.write(f"O'Tooley: {otooley_percentage} ({otooley_votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")