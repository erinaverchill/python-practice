# Your task is to create a Python script that analyzes the records to calculate each of the following:

# Import dependencies
import os
import pandas as pd 

# create file path for csv
budget_file = '~/Documents/gitrepos/homework/python-challenge/PyBank/03-Python_Instructions_PyBank_Resources_budget_data.csv'

# read the csv using pandas + create dataframe
budget_df = pd.read_csv(budget_file)

# The total number of months included in the dataset
total_months = len(budget_df.Date)
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')

#create an empty list to store the MoM changes
month = []
profit_loss = []
monthly_diff = []

# create a new value with the MoM changes - going to need to use LOC here
for i in range(0,total_months): # for every number in the row index
	if i - 1 >= 0:
		monthly_diff.append(budget_df.loc[i,'Profit/Losses'] - budget_df.loc[i-1,'Profit/Losses'])
	else:
		monthly_diff.append(0)

# add the calculated field to the dataframe
budget_df['MoM Change'] = monthly_diff

# The net total amount of "Profit/Losses" over the entire period
net_total = budget_df['Profit/Losses'].sum()
print(f"Total: {net_total}")

# The average of the changes in "Profit/Losses" over the entire period
avg_chg = budget_df['MoM Change'].mean()
rounded_average = round(avg_chg,2)
print (f'Average Change: ${rounded_average}0')

# The greatest increase in profits (date and amount) over the entire period
max_profit = budget_df['MoM Change'].max()
max_loss = budget_df['MoM Change'].min()
for i in range(0,total_months):
	if budget_df.loc[i,'MoM Change'] == max_profit:
		month = budget_df.loc[i,'Date']
		print(f'Greatest increase in profits: {month} (${max_profit})')
	elif budget_df.loc[i,'MoM Change'] == max_loss:
		month = budget_df.loc[i,'Date']
		print(f'Greatest decrease in profits: {month} (${max_loss})')


# find the value in index column 0 for the row where column 2 value = max_profit
#print #date #amount

# The greatest decrease in losses (date and amount) over the entire period
#max_loss = budget_df['Profit/Losses'].min()
#print #date #amount




