import csv
from pathlib import Path

csvpath = Path("budget_data.csv")
csvfile = {}
full_list = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        # test data
        # print(row)
        full_list = full_list + row

# split list into two halves
date = full_list[::2]
profits = full_list[1::2]
print(date)
print(profits)
print(type(profits[0]))

# Converting list of strings to list of integers and skipping first item 'Profit/Losses'
profits = list(map(int, profits[1:]))

#skipping 'Date' header and merging 2 lists into a dictionary
full_books = dict(zip(date[1:], profits))
print(full_books)

#total months
total_months = len(full_books)
#print(total_months)

#sum
#print(sum(full_books.values()))

# get net average change
average_change = (profits[0] - profits[total_months - 1]) / total_months


# find change in profit
counter = 0
m_total = []
while counter < len(profits[:85]):
    # avoid counting 0 to first value
    change = profits[counter +1] - profits[counter]
    
    counter += 1
    
    m_total.append(change)
    #print(len(m_total))
    
    print(change)

    
    print(counter)

# min and max change    
#print(min(m_total))
#print(max(m_total))

def terminal_f():
    return "Financial Analysis"    
    return "--------------------------------"
    
    return total_months
    
    return average_change
    return min(m_total)
    return max(m_total)
    
output = terminal_f()
file = open("Financial_Analysis.txt","w")
file.write("Financial Analysis")
file.write("-------------------")
file.close()