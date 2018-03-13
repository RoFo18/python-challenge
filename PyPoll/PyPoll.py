#import depeendencies
import pandas as pd

# Read in CSV File
csv_path = "../Desktop/Github/election_data_1.csv" and "../Desktop/Github/election_data_2.csv"


poll_df = read_csv(csv_path)
#Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


#The total number of votes cast
total_votes = poll_df["Voter ID"].total()

#A complete list of candidates who received votes The percentage of votes each candidate won

#The total number of votes each candidate won The winner of the election based on popular vote.
