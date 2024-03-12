import pandas as pd

df = pd.read_json('data.json')
#print(df.to_string())

#print(df.head()) #It returnes the first five lines.
#print(df.head(10)) #It returnes the first 10 lines.

#print(df.tail()) #It returnes the last five lines.
#print(df.tail(10)) #It returnes the last 10 lines.

print(df.info()) #It shows more information about the dataframe.