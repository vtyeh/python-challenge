import os
import csv
import re
from datetime import datetime


boss_path = os.path.join("raw_data", "employee_data2.csv")
output_path = os.path.join("../PyBoss", "solved_like_a_boss_2.csv")

# Create empty lists to store data and manipulate
emp_id = []

name = []
first_name = []
last_name = []

date = []
new_date = []

ssn = []
ssn_1 = []
ssn_2 = []
ssn_3 = []
new_ssn = []

state = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
state_abbrev = {v: k for k, v in us_state_abbrev.items()} #Flip key and value for later use
new_state = []

with open(boss_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile, None)

    # The Name column should be split into separate First Name and Last Name columns.
    for row in csvreader:
        emp_id.append(row[0])
        name.append(row[1].split(" "))
        date.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

        for a in name:
            first_name.append(a[0])
            last_name.append(a[1])

    # The DOB data should be re-written into DD/MM/YYYY format from YYYY/DD/MM
    for d in range(len(date)):
        new_date.append((datetime.strptime(date[d], '%Y-%m-%d').strftime('%d/%m/%Y')))

    # The SSN data should be re-written such that the first five numbers are hidden from view.
    # Use regex (regular expression) function for specified formatting
    # \d signifies any alphanumeric character (can also use [0-9]). {} is how many characters.
    for c in range(len(ssn)):
        new_ssn.append(re.sub('\d{3}-\d{2}', '***-**', ssn[c]))

    # The State data should be re-written as simple two-letter abbreviations.
    for s in range(len(state)):
        for key, value in state_abbrev.items():
            if state[s] in value:
                new_state.append(key)

#Create new csv file
with open(output_path, "w", newline='') as csvfile:

    # Initialize the csv writer
    boss_writer = csv.writer(csvfile, delimiter=',')

    #Write the first row for column headers
    boss_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    #Zip lists together and write a row in csvfile for each row
    new = zip(emp_id, first_name, last_name, new_date, new_ssn, new_state)
    for row in new:
        boss_writer.writerow(row)
