import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import seaborn as sns             


columns = ['CustomerID','Gender','Age','Annual Income ','Spending Score '] #load data
data=pd.read_csv(r"C:\Users\user\Desktop\bh\Mall_Customers.csv",encoding='latin1')
print(data)
print(data.isnull().sum())
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])
print(data.head())
X=data.iloc[:,[3,4]].values       #cluster
print(X)

wcss=[]
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) 
print(wcss)

    #elbow graph
sns.set()
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method For Optimal Number of Clusters')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()

clusters=5
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=42)
y=kmeans.fit_predict(X)
print(y)
clusters=0,1,2,3,4
plt.figure(figsize=(8,8))
plt.scatter(X[y==0,0],X[y==0,1],s=50,c='blue',label='cluster 1')
plt.scatter(X[y==1,0],X[y==1,1],s=50,c='green',label='cluster 2')
plt.scatter(X[y==2,0],X[y==2,1],s=50,c='pink',label='cluster 3')
plt.scatter(X[y==3,0],X[y==3,1],s=50,c='black',label='cluster 4')
plt.scatter(X[y==4,0],X[y==4,1],s=50,c='gray',label='cluster 5')

#centroids

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='red',label='centroids')
plt.title('customer group')
plt.xlabel('annual income')
plt.show()