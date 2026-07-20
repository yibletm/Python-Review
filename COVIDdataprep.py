import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import os
from sklearn.ensemble import RandomForestRegressor
import warnings as wr
wr.filterwarnings('ignore')
ds = pd.read_csv("COVID19_Statistics_200_Rows-1.csv")
missing_values = ds.isnull().sum()
print(missing_values)
ds = ds.drop_duplicates()
ds.info()

lb=LabelEncoder()

ds['Date'] = lb.fit_transform(ds['Date'])
ds['Country'] = lb.fit_transform(ds['Country'])
ds['State'] = lb.fit_transform(ds['State'])

corrmat = ds.corr(numeric_only=True)
correlations=ds.corr()['Recovered'].abs().sort_values()
Low_corr= correlations.head(3).index.tolist()
print(corrmat)
print(Low_corr)
ds = ds.drop(columns=Low_corr)

x = ds.drop('Recovered', axis=1)
y = ds['Recovered']
print(y.shape)
print(x.head())



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

scaler = StandardScaler()
print(x_train) #All values in x_train are numeric
scal_x_train = scaler.fit_transform(x_train) #calculates the current mean and standard deviation
scal_x_test = scaler.transform(x_test) #Calculates the previous mean and std dev

model = LinearRegression() #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = r2_score(y_test, y_pred)
print(f"Logistic regression accuracy: {acc:.4f}")

regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(scal_x_train, y_train)
y_pred = regressor.predict(scal_x_test)
accuracy = r2_score(y_test, y_pred)
print(f'Random forest Accuracy: {accuracy * 100:.2f}%')

#print(ds.duplicated().sum())

Train_acc= r2_score(y_train, model.predict(scal_x_train))
Test_acc= r2_score(y_test, model.predict(scal_x_test))
print(Train_acc)
print(Test_acc)
print(Train_acc-Test_acc)



