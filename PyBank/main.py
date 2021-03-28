# Import modules
import os
import csv

# Set initial variables
month_count = 0
net_profit = 0
previous_month_profit = 0

# Lists to store data
profit_changes_list = []
date_list = []


# Set path of file to read
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

# Open budget_data.csv to read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row in the .csv
    csv_header = next(csvreader)  

    #For each row in the .csv file starting from the second row
    for row in csvreader:
        # Count Months
        month_count += 1

        # Create a list of dates in the data
        date_list.append(row[0])

        # Add up profit and losses for each month
        current_month_profit = int(row[1])
        net_profit += current_month_profit

        # Calculate the profit change between each month
        profit_change = current_month_profit - previous_month_profit

        # Add the profit change to the profit changes list
        profit_changes_list.append(profit_change)

        # Set the previous months profit value
        previous_month_profit = current_month_profit
        
        
# Create function to calculate average
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total = total + number
    return total / length

# use previous function to calculate average profit change to 2 decimal places
average_profit_change = round(average(profit_changes_list[1:86]), 2)


# Find greatest increase in profits
greatest_profit_increase = max(profit_changes_list)
# Find date of greatest increase in profits
greatest_increase_date = date_list[profit_changes_list.index(greatest_profit_increase)]
     
# Find greatest decrease in profits
greatest_profit_decrease = min(profit_changes_list)
# Find month of greatest decrease in profits
greatest_decrease_date = date_list[profit_changes_list.index(greatest_profit_decrease)]


# Print financial analysis in terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_profit_decrease})")


# Create .txt file with financial analysis in Analysis folder
with open (os.path.join(dirname, 'Analysis', 'financial_analysis.txt'), 'w') as file:

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${average_profit_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_profit_decrease})\n")