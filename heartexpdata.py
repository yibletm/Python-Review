#Step 1: Importing Libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

#Step 2: Reading Data
df = pd.read_csv("heart.csv")


#Step 3 data analysis
print(df.head())
print(df.shape)
print(df.info())
print(df.corr())
corrs = df.corr()['target'].abs().sort_values()
print(corrs.tail(3).index.tolist())

#Step 4: Missing Value Checking

print(df.isnull().sum())

#Step 5: Duplicate checking

print(df.duplicated().sum())

#Step 6: Univariate Analysis
#Boxplot
target_counts = df['target'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(target_counts.index, target_counts, color='deeppink')
plt.title('Count Plot of the presence of heart disease')
plt.xlabel('Heart disease amount')
plt.ylabel('Count')
plt.show()

#Swarm Plot
plt.figure(figsize=(10, 8))

sns.swarmplot(x="thalach", y="age", data=df, palette='viridis')
plt.title('Swarm Plot for max heart rate and Age')
plt.xlabel('Max Heart rate')
plt.ylabel('Age')
plt.show()