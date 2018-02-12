import os
import csv

budget_path = os.path.join("raw_data", "budget_data_2.csv") # Change path to desired folder and csv file

print("Financial Analysis")
print("------------------")

#   Create empty lists to store new lists
total_months = []
total_revenue =[]
avg_rev =[]

revenue = 0
index = 0

with open(budget_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile, None)

    # Calculate total number of months
    for row in csvreader:
        total_months.append(row[0])
        total = len(list(total_months))

        # Calculate total amount of revenue gained over entire period
        revenue += int(row[1])
        total_revenue.append(row[1])
    print("Total Months: " + str(total))
    print("Total Revenue: $" + str(revenue))

    # Calculate average change in revenue between months
    for i in range(len(total_revenue)):
        if i < (len(total_revenue)-1):
            avg_rev.append(int(total_revenue[i+1])-int(total_revenue[i]))
        y = sum(avg_rev)/int(len(avg_rev))
    print("Average Change in Revenue: ${:.0f}".format(y))

    # Index for total_revenue is 0-40 and index for avg_rev is 0-39
    # Calculate greatest increase in revenue (date and amount)
    greatest_increase = max(avg_rev)
    for z in avg_rev:
        if z == greatest_increase:
            max_date = int(avg_rev.index(z)) + 1

            print("Greatest Increase in Revenue: " + str(total_months[max_date]) +
                  " ($" + str(greatest_increase) + ")")


    # Calculate greatest decrease in revenue (date and amount)
    greatest_decrease = min(avg_rev)
    for a in avg_rev:
        if a == greatest_decrease:
            min_date = int(avg_rev.index(a)) + 1

            print("Greatest Decrease in Revenue: " + str(total_months[min_date]) +
                  " ($" + str(greatest_decrease) + ")")
