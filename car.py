import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

columns = ['buying','maint','doors','person','lug_boot','safety','class'] #load data
data=pd.read_csv(r"C:\Users\user\Desktop\bh\car (1).data",encoding='latin1',names=columns)
print(data)
print(data.isnull().sum())   # checking for missing values
X= data[['buying','maint','doors','person','lug_boot','safety']] #split
y=data['class']
X_encoded = pd.get_dummies(X)       #encode x
le = LabelEncoder()                   #encode y
y_encoded = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)    # Split data into training and test sets
model = LogisticRegression()       # Create and train the logistic regression model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)     #  Make predictions on the test set
accuracy = accuracy_score(y_test, y_pred)      # Evaluate model accuracy
print(f"Accuracy: {accuracy:.2f}")