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


#Step 4: Missing Value Checking

print(df.isnull().sum())

#Step 5: Duplicate checking

print(df.duplicated().sum())