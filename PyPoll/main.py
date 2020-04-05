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
print('Election Results:')
print('--------------------------')
print(f'Total votes cast: {total_votes}')
print('--------------------------')

# A complete list of candidates who received votes
candidates = election_data_df.Candidate.unique()
#print(f'Candidates who recieved votes: {candidates}')

# The total number of votes each candidate won
votes_per_candidate = election_data_df.Candidate.value_counts()

khan = votes_per_candidate['Khan']
correy = votes_per_candidate['Correy']
li = votes_per_candidate['Li']
o_tooley = votes_per_candidate["O'Tooley"]

khan_percent = (khan / total_votes) * 100
correy_percent = (correy / total_votes) * 100
li_percent = (li / total_votes) * 100
o_tooley_percent = (o_tooley / total_votes) * 100

print('Votes per candidate:')
print('--------------------------')
print(f'Khan: {khan} votes ({round(khan_percent, 2)}%)')
print(f'Correy: {correy} votes ({round(correy_percent,2)}%)')
print(f'Li: {li} votes ({round(li_percent,2)})%')
print(f"O'Tooley: {o_tooley} votes ({round(o_tooley_percent,2)}%)")
print('The winner is Khan')






