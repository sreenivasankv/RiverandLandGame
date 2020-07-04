#########Step1############
import pandas as pd
data = pd.read_csv("Task_Training_Data .csv")
print("Name:Email")
for index, row in data.iterrows():
    print(row['Name'], ":", row['Email'])
