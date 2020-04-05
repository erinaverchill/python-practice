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
print(f'Total votes cast: {total_votes}')

# A complete list of candidates who received votes
candidates = election_data_df.Candidate.unique()
print(f'Candidates who recieved votes: {candidates}')

# The total number of votes each candidate won
khan = election_data_df.Candidate.valuecount()

#'Correy' 'Li' "O'Tooley"







