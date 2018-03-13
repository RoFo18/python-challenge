
# Read in CSV File
import os
import csv 

#use brackets to combine the two CSV data sets
csv_path = ["../Desktop/Github/budget_data_1.csv" , "../Desktop/Github/budget_data_2.csv"]

Bank_df = read_csv(csv_path)
total_months = bank_df["months"].total()
total_revenue = bank_df["Revenue"].total()
#Average revenue change between months
average_revenue_change = bank_df["Revenue"].mean()
#The greatest increase in revenue (date and amount) over the entire period
mac_positive_revenue_change = bank_df["Revenue"].max()
#The greatest decrease in revenue (date and amount) over the entire period
max_negative_revenue_change = bank_df["Revenue"].min()


print
