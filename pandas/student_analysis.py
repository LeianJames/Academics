import pandas as pd
import numpy as np

data = pd.read_csv("students.csv")

data['Final_Grade'] = (data['Prelim'] + data['Midterm'] + data['Finals']) / 3   # --> Average of all 3 major examinations

# print(data['Final_Grade'])                 # ---> For testing if Final_Grade works properly

data['Status'] = np.where(data['Final_Grade'] >= 75, "Passed", "Failed")        #--> np.where(condition, value_if_true, value_if_false)

# print(data['Status'])                     # ---> For testing if data['Status] works properly



group = data.groupby('Program')['Final_Grade'].mean()                          #--> Computes the average for each program/courses
year_level_performance = data.groupby('Year_Level').apply(                     #--> Groups by Year Level
    lambda x: (x['Status'] == "Passed").sum() / len(x) * 100 )                 #--> Calculates the percentage of students passed
# print(group)                                              
# print(year_level_performance)

Ranking = data.nlargest(5, "Final_Grade")                                      #--> Isolates the top 5 scorers
# print(Ranking)

subject_means = data[["Prelim", "Midterm", "Finals"]].mean()                   #--> Calculates the average for each Major Examination
print(subject_means)

bsit_passed = data[(data['Program'] == "BSIT") & (data["Status"] == "Passed")]  #--> Boolean Indexing to locate BSIT students who passed
# print(bsit_passed)

honors = data[data["Final_Grade"] > 90]                         #--> New DataFrame only of students with a Final_Grade above 90.
# print(honors)