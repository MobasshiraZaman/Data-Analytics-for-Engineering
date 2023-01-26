# Homework 2
# Mobasshira Zaman


import pandas as pd
# Importing local file and saving as a dataframe
data = pd.read_csv(r'data/Food_Inspections.csv')
# 2
print('Number of rows:',len(data))

# 5
Col= data.columns
c= []
for i in range(0,16):
    cardinality= data[Col[i]].value_counts()
    c.append(cardinality)
    print(i,":",cardinality)
df= {'col': Col,
     'values': c }

