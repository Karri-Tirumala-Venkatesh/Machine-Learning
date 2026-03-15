import pandas as pd

# Creating a Dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
})

print(df)

'''

# Print first 5 rows
df.head()

#Data types & Memory Usage
df.info()

#Statistical Summary of the Dataset
df.describe()

#Reading from a file
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

#Saving the data
df = pd.to_csv("data.csv")
df.to_excel("data.xlsx")

#Changing Data type
df['Date'] = pd.to_datetime(df['Date'])
df['Age'] = df['Age'].astype(int)

#Remove rows with incomplete data
df.dropna()

#Adding new columns - Row wise operation
df['Col2']=df['Col1']+1

'''