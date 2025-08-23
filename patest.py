import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)

# data={'Name':['Alice','Bob'],'Age':[25,30]}
# df=pd.DataFrame(data)
# print(df)

#df.head()

# data={
#     'Name':['Alice','Bob','charlie','anu','neha','adhee'],
#       'Age':[25,30,33,24,56,12]
#       }
# df=pd.DataFrame(data)
# print(df.head())
# print(df.head(3))


#df.tail()
# print(df.tail())
# print(df.tail(2))

#df.info()


data={
    'Name':['Alice','Bob','charlie','anu','neha','adhee'],
      'Age':[25,30,33,24,56,None],
      'score':[85.5,90,70,60,80,67]
      }
df=pd.DataFrame(data)
# df.info()


#df.describe()

# print(df.describe())

#df.columns

# print(df.columns)

#df.shape

# print(df.shape)

#df.loc[]

# df=pd.DataFrame(data,index=['a','b','c','d','e','f'])
# print(df.loc['a'])
# print(df.loc['b','Name'])
# print(df.loc[:, ['Name','score']])

# print(df.iloc[0])
# print(df.iloc[1,0])
# print(df.iloc[:, 0:2])

#null

# df=pd.DataFrame(data)
# print(df.isnull())

#df.dropna to drop null values
df=pd.DataFrame(data)
print(df.dropna())