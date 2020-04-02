# Your task is to create a Python script that analyzes the records to calculate each of the following:

# Import dependencies
import os
import pandas as pd 

# create file path for csv
budget_file = '~/Documents/gitrepos/homework/python-challenge/PyBank/03-Python_Instructions_PyBank_Resources_budget_data.csv'

# read the csv using pandas
budget_df = pd.read_csv(budget_file)

# The total number of months included in the dataset
total_months = len(budget_df.Date)
print(total_months) # update this to print a string

# The net total amount of "Profit/Losses" over the entire period
net_total = budget_df['Profit/Losses'].sum()
print(net_total) # update this to print a string

# The average of the changes in "Profit/Losses" over the entire period
# do you want to create a new column with the MoM changes?
# average_chg = budget_df['Profit/Losses'].mean()
# print(average_chg)

# The greatest increase in profits (date and amount) over the entire period
max_profit = budget_df['Profit/Losses'].max()
print #date #amount

# The greatest decrease in losses (date and amount) over the entire period
max_loss = budget_df['Profit/Losses'].min()
print #date #amount



