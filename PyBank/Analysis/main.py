#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period 
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")


total_month = 0
total_revenue = 0 
revenue_changes = []
revenue_change = []
prev_revenue = 0
avg_change = 0
greatestInc = 0
greatestDec = 0
greatest_month = ""
lowest_month = ""

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:


#Revenue Changes 
        total_month = total_month + 1
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])

        revenue_changes = revenue_changes + [revenue_change]
    

# Find value and month of greatest increase and decrease 

        if revenue_change > greatestInc:
            greatestInc = revenue_change
            greatest_month = row[0]


        if revenue_change < greatestDec:
            greatestDec = revenue_change
            lowest_month = row[0]

# Calculate the Average Revenue Change 

    revenue_changes = revenue_changes[1:]

    print(revenue_changes)
    avg_change = round((sum(revenue_changes)) /(len(revenue_changes)))




print(f"Financial Analysis")
print(f"----------------------")
print(f"Total months: " + str(total_month))
print(f"Total: " "$"+str(total_revenue))
print(f"Average Change:" "$"+str(avg_change))
print(f"Greatest Increase in Profits:", (greatest_month), "$"+str(greatestInc))
print(f"Greatest Decrease in Profits:", (lowest_month), "$"+str(greatestDec))

#Output File 

pybank_output = os.path.join("Analysis", "budget_analysis.txt")

with open (pybank_output, 'w') as txtfile:

    txtfile.write(f"Financial Analysis \n")
    txtfile.write(f"---------------------- \n")
    txtfile.write(f"Total months: {total_month}\n")
    txtfile.write(f"Total Revenue: $ {total_revenue}\n")
    txtfile.write(f"Average Change: $ {avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_month} ${(greatestInc)}\n")
    txtfile.write(f"Greatest Decrease in Profits: {lowest_month} ${greatestDec}\n")














