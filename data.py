import pandas as pd
data={
    'Name':['Alice','Bob','charlie','anu','neha'],
      'Age':[25,30,33,24,None],
      'score':[85.5,90,70,60,80]
      }
df=pd.DataFrame(data)
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)