import numpy as np
import random

daily_sales = np.random.randint(1,101, size = 50)   #--> (representing items sold per day).

total_sales = np.sum(daily_sales)                   #--> Calculates the Total Sales for the entire 50-day period

average_daily_sale = np.mean(daily_sales)           #--> Determines the average daily sales

best_day = np.max(daily_sales)                      #--> Calculates the best sales day
worst_day = np.min(daily_sales)                     #--> Calculates the worst sales day


print(f"Items sold: \n {daily_sales}")              #Output verification
print()                                             #Prints out new line for readability
print(f"Total sales: {total_sales}")                
print(f"Average sale: {average_daily_sale}")
print(f"best sales day: {best_day}")
print(f"worst sales day: {worst_day}")
print()

mask = (daily_sales > average_daily_sale)           #identifies high performance days
print(f"High Performance Days: {daily_sales[mask]}")
print(f"Total High Performance Days: {daily_sales[mask].size}") #counts how many high performance days there are