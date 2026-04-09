import pandas as pd

df = pd.read_csv("students.csv")        #---> Loads the file into a dataframe (csv was made on google sheets)

print(df.info())                        #---> check data types
print(df.shape)                         #---> verify the record count (20 rows, 7 columns)
print(df.isnull().sum())                #---> checks for empty cells

df.dropna(inplace=True)                 #--->  drop the row if empty cells