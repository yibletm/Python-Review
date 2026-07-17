import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
from sklearn.ensemble import RandomForestClassifier
ds = pd.read_csv("COVID19_Statistics_200_Rows-1.csv")
missing_values = ds.isnull().sum()
print(missing_values)
ds = ds.drop_duplicates()
ds.info()

x = ds.drop('Vaccination_Rate_%', axis=1)
y = ds['Vaccination_Rate_%']
print(y.shape)
print(x.head())

lb=LabelEncoder()

x['data'] = lb.fit_transform(x['data'])
x['Country'] = lb.fit_transform(x['Country'])
x['State'] = lb.fit_transform(x['State'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

scaler = StandardScaler()
print(x_train) #All values in x_train are numeric
scal_x_train = scaler.fit_transform(x_train) #calculates the current mean and standard deviation
scal_x_test = scaler.transform(x_test) #Calculates the previous mean and std dev

model = LogisticRegression(max_iter=200) #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Logistic regression accuracy: {acc:.4f}")

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(scal_x_train, y_train)
y_pred = classifier.predict(scal_x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Random forest Accuracy: {accuracy * 100:.2f}%')

print(ds.duplicated().sum())

Train_acc= accuracy_score(y_train, model.predict(scal_x_train))
Test_acc= accuracy_score(y_test, model.predict(scal_x_test))
print(Train_acc)
print(Test_acc)
print(Train_acc-Test_acc)



