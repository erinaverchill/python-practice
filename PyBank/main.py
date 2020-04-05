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




# create a new value with the MoM changes - going to need to use LOC here?
# nested for loop? 

# calculate the MoM changes 
for i in range(1,total_months): # for every number in the row index
	if i - 1 > 0:
		monthly_diff.append(budget_df.loc[i,'Profit/Losses'] - budget_df.loc[i-1,'Profit/Losses'])
	else:
		monthly_diff.append(0)

budget_df['MoM Change'] = monthly_diff





for
	budget_df.loc[i,'Profit/Losses'] - budget_df.loc[i-1,'Profit/Losses']





print(total_months) # update this to print a string

# The net total amount of "Profit/Losses" over the entire period
net_total = budget_df['Profit/Losses'].sum()
print(f"Total: {net_total}")

# The average of the changes in "Profit/Losses" over the entire period

# going to need to us LOC here
for i in range(1, total_months)
	monthly_dif = budget_df.loc[i,'Profit/Losses'] - budget_df.loc[i-1,'Profit/Losses']

# The greatest increase in profits (date and amount) over the entire period
max_profit = budget_df['Profit/Losses'].max()
print #date #amount

# The greatest decrease in losses (date and amount) over the entire period
max_loss = budget_df['Profit/Losses'].min()
print #date #amount




# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be give a set of poll data called election_data.csv. 

# The dataset is composed of three columns: 
	# Voter ID, County, and Candidate. 

# Your task is to create a Python script that analyzes the votes and calculates each of the following:
	# The total number of votes cast
	# A complete list of candidates who received votes
	# The percentage of votes each candidate won
	# The total number of votes each candidate won
	# The winner of the election based on popular vote.

import os
import pandas as pd 
import numpy as np 

# Create file path for csv
election_data_df = pd.read_csv('~/Documents/gitrepos/homework/python-challenge/PyPoll/election_data.csv')

# calculate total number of votes cast
total_votes = len(election_data_df['Voter ID'])

# A complete list of candidates who received votes
candidates = election_data_df.Candidate.unique()

# The total number of votes each candidate won




