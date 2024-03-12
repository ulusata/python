import pandas as pd

df = pd.read_csv('data.csv')
#print(df) #It will not show all of the rows unless 'to_string()' is called.
#print(df.to_string())

#If max_rows value is changed, then it can show up more lines.
#print(pd.options.display.max_rows) #60

#Now max_rows value is being changed here.
pd.options.display.max_rows = 999
#print(pd.options.display.max_rows) #999
print(df)
