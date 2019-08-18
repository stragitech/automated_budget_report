import csv
from pathlib import Path

csvpath = Path("budget_data.csv")
csvfile = {}
full_list = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        full_list = full_list + row

# split list into two halves
date = full_list[::2]
profits = full_list[1::2]

# Converting list of strings to list of integers and skipping first item 'Profit/Losses'
profits = list(map(int, profits[1:]))

#skipping 'Date' header and merging 2 lists into a dictionary
full_books = dict(zip(date[1:], profits))

#get number of months
total_months = len(full_books)

#get sum of profit values
full_sum = sum(full_books.values())


# get net average change
average_change = (profits[0] - profits[total_months - 1]) / (total_months -1)

# find change in profit
counter = 0
m_total = []
while counter < len(profits[:85]):
    # avoid counting 0 to first value
    change = profits[counter +1] - profits[counter]
    
    counter += 1
    
    m_total.append(change)

# get max and min
min_m_total = min(m_total)
max_m_total = max(m_total)

# cast integers to strings
min_val = str(min_m_total)
max_val = str(max_m_total)
months = str(total_months)
total = str(full_sum)
avg = str(average_change)

#open file and write output in file
with open("Financial_Analysis.txt", "w") as file:
    file.write("Financial_Analysis" + "\n")
    file.write("----------------------" + "\n")
    file.write("Total Months: " + months+ "\n")
    file.write("Total: $" + total + "\n")
    file.write("Average Change: -$" + avg + "\n")      
    file.write("Greatest Increase in Profits " + max_val + "\n")
    file.write("Greatest Decrease in Profits " + min_val + "\n")

#read output from written file
with open("Financial_Analysis.txt", "r") as file_r:
    for line in file_r:
        print(line, end = '')