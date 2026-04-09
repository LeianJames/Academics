import numpy as np

#branches = rows
#weeks = columns

performance_matrix = np.random.randint(1,101, size = (5,5))         #--> creates a 5x5 matrix with values ranging from 1-100

average_branch = np.mean(performance_matrix, axis = 1)              #--> calculates the mean for axis 1 (rows)
average_weeks = np.mean(performance_matrix, axis = 0)               #--> calculates the mean for axis 0 (columns) 

top_performer = np.argmax(average_branch)                           #--> identify the index of the highest-performing store.
lowest_overall = np.argmin(average_weeks)                           #--> Identify the Week  with the lowest overall average.

slice_column = performance_matrix[:, lowest_overall]                #--> selects the lowest overall column
efficiency_bonus = slice_column * 1.10                              #--> Apply a 10% Efficiency Bonus to that column

mask = np.all(performance_matrix > 70, axis = 1)                    #--> find branches that scrored above 70 in every single week
count = np.sum(mask)                                                #--> counts the "True" values 



print()
print(performance_matrix)                                          #prints out the matrix 
print()                                                            #newline
print(f"average score for each branch: {average_branch}")
print(f"average score for each week: {average_weeks}")           
print()   
print(f"index of the highest performing store: {top_performer}")
print(f"index of the week with the lowest overall: {lowest_overall}")
print(f"Applied a 10% efficiency bonus to the lowest week: {efficiency_bonus}")
print(f"\nBranches that scored above 70: {count} ")