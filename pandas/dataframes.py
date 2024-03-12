import pandas as pd

data = {
        'books': ['A', 'B', 'C'],
        'pages': [250, 120, 300]
    }

df = pd.DataFrame(data)
#print(df)
#print(df.loc[1]) #This code returns a pandas series
#print(df.loc[0:]) #This code returns a pandas dataframe
indexNo = ['x', 'y', 'z']
df = pd.DataFrame(data, index = indexNo)
#print(df.loc['x']) #loc object returns value according to the index. Index numbers can be changed and it will effect loc object.

df = pd.read_csv('data.csv') #Reading and loading a csv file and assigning it to a dataframe object.
#print(df)