import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import os
#Loading the iris dataset
titanic = pd.read_csv("Titanic-Dataset.csv")
titanic_df = sns.load_dataset('titanic')

#next is for checking for any missing values

#print(titanic_df.describe())

# Dealing with missing values 

missing_values = titanic_df.isnull().sum()
#print(missing_values)

# Dropping columns with excessive missing data
new_titanic_df = titanic_df.drop(columns=['deck'])

# Imputing median age for missing age data
new_titanic_df['age'] = new_titanic_df['age'].fillna(new_titanic_df['age'].median())

# Display the number of missing values post-imputation
missing_values_updated = new_titanic_df.isnull().sum()
#print(missing_values_updated)

x = new_titanic_df.drop('survived', axis=1) # drop removes the entirity of specifically the Survived column (while axis depicts how many columns)
#doesn't change data only applies them and assigns the changed set as x

y = new_titanic_df['survived']
print(y.shape)

lb = LabelEncoder()
x['sex'] = lb.fit_transform(x['sex'])
x['embarked'] = lb.fit_transform(x['embarked'])
x['class'] = lb.fit_transform(x['class'])
x['who'] = lb.fit_transform(x['who'])
x['adult_male'] = lb.fit_transform(x['adult_male'])
x = x.drop('embark_town', axis=1)
x['alive'] = lb.fit_transform(x['alive'])
x['alone'] = lb.fit_transform(x['alone'])
enc_y = lb.fit_transform(y) #fit_transform
#after encoding, then you split the variables into 

#the ordering for the different x and y values matters a whole lot.

x_train, x_test, y_train, y_test = train_test_split(x, enc_y, test_size=0.2, random_state=42)

scaler = StandardScaler() #fit_transform applies standardization
print(x.head())
scal_x_train = scaler.fit_transform(x_train)
scal_x_test = scaler.fit_transform(x_test)

model = LogisticRegression(max_iter=200) #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {acc:.4f}")
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import os

#Loading the iris dataset
titanic = pd.read_csv("Titanic-Dataset.csv")
titanic_df = sns.load_dataset('titanic')

#next is for checking for any missing values

#print(titanic_df.describe())

# Dealing with missing values 

missing_values = titanic_df.isnull().sum()
#print(missing_values)

# Dropping columns with excessive missing data
new_titanic_df = titanic_df.drop(columns=['deck'])

# Imputing median age for missing age data
new_titanic_df['age'] = new_titanic_df['age'].fillna(new_titanic_df['age'].median())

# Display the number of missing values post-imputation
missing_values_updated = new_titanic_df.isnull().sum()
#print(missing_values_updated)

x = new_titanic_df.drop('survived', axis=1) # drop removes the entirity of specifically the Survived column (while axis depicts how many columns)
#doesn't change data only applies them and assigns the changed set as x

y = new_titanic_df['survived']
print(y.shape)

print(x.head())
lb = LabelEncoder()
#fit_transform turns the values into numbers
x['sex'] = lb.fit_transform(x['sex'])
x['embarked'] = lb.fit_transform(x['embarked'])
x['class'] = lb.fit_transform(x['class'])
x['who'] = lb.fit_transform(x['who'])
x['adult_male'] = lb.fit_transform(x['adult_male'])
x = x.drop('embark_town', axis=1)
x['alive'] = lb.fit_transform(x['alive'])
x['alone'] = lb.fit_transform(x['alone'])
enc_y = lb.fit_transform(y) #fit_transform
#after encoding, then you split the variables into 

#the ordering for the different x and y values matters a whole lot.

x_train, x_test, y_train, y_test = train_test_split(x, enc_y, test_size=0.4, random_state=42)

scaler = StandardScaler() #fit_transform applies standardization (which can only work with non-strings: requires encoding string values)
print(x.head())
scal_x_train = scaler.fit_transform(x_train)
scal_x_test = scaler.fit_transform(x_test)

model = LogisticRegression(max_iter=200) #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {acc:.4f}")