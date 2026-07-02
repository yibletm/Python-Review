import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
#Loading the iris dataset
iris = pd.read_csv("Iris.csv")

#next is for checking for any missing values

print(iris.isnull().sum())

x = iris.drop('Species', axis=1) # drop removes the entirity of specifically the species column (while axis depicts how many columns)
#doesn't change data only applies them and assigns the changed set as x

y = iris['Species']

lb = LabelEncoder()
enc_y = lb.fit_transform(y) #fit_transform

#after encoding, then you split the variables into 

#the ordering for the different x and y values matters a whole lot.

x_train, x_test, y_train, y_test = train_test_split(x, enc_y, test_size=0.2, random_state=42)

scaler = StandardScaler() #fit_transform applies standardization
scal_x_train = scaler.fit_transform(x_train)
scal_x_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=200) #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {acc:.4f}")
