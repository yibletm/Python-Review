import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
from sklearn.ensemble import RandomForestClassifier
heart = pd.read_csv("heart.csv")
missing_values = heart.isnull().sum()
print(missing_values)
heart = heart.drop_duplicates()
heart.info()

x = heart.drop('target', axis=1)
y = heart['target']
print(y.shape)
print(x.head())

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

print(heart.duplicated().sum())

Train_acc= accuracy_score(y_train, model.predict(scal_x_train))
Test_acc= accuracy_score(y_test, model.predict(scal_x_test))
print(Train_acc)
print(Test_acc)
print(Train_acc-Test_acc)




data = {'trestbps': ['0', '1', '2', '3']}

heart_encoded = pd.get_dummies(heart, columns=['cp'], prefix='cp')
print(heart_encoded)

trestbps = heart['trestbps']

print(trestbps.head())

max = trestbps[0]
min = trestbps[0]
for i in trestbps:
    if i>max:
        max = i
    if i<min:
        min = i

bins = [80, 100, 120, 140, 160, 180, 200]
labels = [0, 1, 2, 3, 4, 5]

heart['trestbps_set'] = pd.cut(heart['trestbps'], labels=labels, bins=bins)
heart = heart.drop('trestbps', axis=1)

print(f"Max: {max}, Min: {min}")
x = heart.drop('target', axis=1)
y = heart['target']
print(y.shape)
print(x.head())
print(heart['trestbps_set'])

corrmat = heart.corr(numeric_only=True)
correlations=heart.corr()['target'].abs().sort_values()
Low_corr= correlations.head(3).index.tolist()
print(Low_corr)

heart = heart.drop(columns=Low_corr)
x = heart




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

print(heart.duplicated().sum())

Train_acc= accuracy_score(y_train, model.predict(scal_x_train))
Test_acc= accuracy_score(y_test, model.predict(scal_x_test))
print(Train_acc)
print(Test_acc)
print(Train_acc-Test_acc)

