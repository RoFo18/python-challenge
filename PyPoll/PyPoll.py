# Read in CSV File
import os
import csv 

csv_paths = ["../Desktop/Github/election_data_1.csv", "../Desktop/Github/election_data_2.csv"]


for csv_path in csv_paths:

with open([PyPoll_csv, encoding "UTF=8", newline="") as csvfile:
    csvreader =csv.reader(scvfiler, delimiter =",")

    

poll_df = read_csv(csv_path)
#Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
total_votes = poll_df["Voter ID"].total()

#A complete list of candidates who received votes The percentage of votes each candidate won

candidate_list = poll_df["Candidate"].list()

#The total number of votes each candidate won The winner of the election based on popular vote.


