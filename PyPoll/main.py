# Import modules for reading csv and navigating file path
import os
import csv

# Create placeholder variables and lists for final analysis
total_votes = 0
candidates_list =[]
unique_candidates_list =[]
votes_for_candidate = [0, 0, 0]

# Create path to find election_data.csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
            
    # Read the header row first
    csv_header = next(csvreader)
                    
    #loop through rows count the total rows (votes) create a list of candidates
    for row in csvreader:
        total_votes += 1
        candidates_list.append(row[2])

# create a list of unique candidates    
for candidate in candidates_list:
    if candidate not in unique_candidates_list:
        unique_candidates_list.append(candidate)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
                    
    #loop through rows    
    for vote in csvreader:
        if vote[2] == unique_candidates_list[0]:
            votes_for_candidate[0] +=1
        elif vote[2] == unique_candidates_list[1]:
            votes_for_candidate[1] +=1
        elif vote[2] == unique_candidates_list[2]:
            votes_for_candidate[2] +=1    

#store variables for final analysis calculations and formatting
winning_votes = max(votes_for_candidate)
winner = unique_candidates_list[(votes_for_candidate.index(winning_votes))]
percentages = [x / total_votes for x in votes_for_candidate]
formatted_percentage = ["{:.3%}".format(y) for y in percentages]
final_results = dict(zip(unique_candidates_list, zip(formatted_percentage, (votes_for_candidate))))

# create file path to store txt file in analysis folder
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

# write final analysis to text file that was created
with open(output_path, 'w') as analysisfile:
    analysisfile.write("Election Results\n")
    analysisfile.write("----------------------------\n")
    analysisfile.write(f"Total Votes: {total_votes}\n")
    analysisfile.write("----------------------------\n")
    
    # Loop through candidates and write results to file
    for candidate, (percentage, votes) in final_results.items():
        analysisfile.write(f"{candidate}: {percentage} ({votes})\n")
        
    analysisfile.write("----------------------------\n")
    analysisfile.write(f"Winner: {winner}\n")
    analysisfile.write("----------------------------")