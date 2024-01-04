# Import modules for reading csv and navigating file path
import os
import csv

# Create placeholder variables for final analysis
# Need to create a list to store changes
total_months = 0
profit_loss = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
changes =[]
months =[]

# Create path to find budget_data.csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
            
    # Read the header row first
    csv_header = next(csvreader)
    
    # Initalizing previous value for calculation change outside of loop 
    previous_value = 0
                
    #loop through rows    
    for row in csvreader:
        
        #loop through rows counting each row and add it to total_months and store months into list
        total_months += 1
        months.append(row[0])
    
        # loop through rows store value and then add to profit_loss variable
        numbers = int(row[1])
        profit_loss += numbers
        
        #loop through rows and calculate the change of the p/l by subtracting the old numbers from the new
        current_value = int(row[1])
        change = current_value - previous_value

        #add change to changes list
        changes.append(change)
        
        # Reset previous value to the current value for next calculation
        previous_value = current_value

# store the variables for the calculate average change, min, max and corresponding month/year values
# used range [1:total months] to skip the first change in the list since there is no actual change value for first month
average_change = format(sum(changes[1:total_months]) / len(changes[1:total_months]), '.2f')
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_month = months[(changes.index(greatest_increase))]
decrease_month = months[(changes.index(greatest_decrease))]

# create file path to store txt file in analysis folder
output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

with open(output_path, 'w') as analysisfile:

    analysisfile.write("Financial Analysis\n")
    analysisfile.write("----------------------------\n")
    analysisfile.write(f"Total Months: {total_months}\n")
    analysisfile.write(f"Total: ${profit_loss}\n")
    analysisfile.write(f"Average Change: {average_change}\n")
    analysisfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    analysisfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")