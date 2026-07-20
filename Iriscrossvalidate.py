from sklearn.model_selection import cross_val_score, KFold
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import os

iris = load_iris()
x, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
scaler = StandardScaler() #fit_transform applies standardization (which can only work with non-strings: requires encoding string values)
scal_x_train = scaler.fit_transform(x_train)
scal_x_test = scaler.fit_transform(x_test)

model = LogisticRegression(max_iter=200) #max_iter (iter means iteration) how many times it iterates through data
model.fit(scal_x_train, y_train)
y_pred = model.predict(scal_x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Logistic Regression accuracy: {acc:.4f}")

regressor = RandomForestClassifier(n_estimators=100, random_state=42)
regressor.fit(scal_x_train, y_train)
y_pred = regressor.predict(scal_x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Random forest Accuracy: {accuracy * 100:.2f}%')

svm_classifier = SVC(kernel='linear')

num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

cross_val_results = cross_val_score(svm_classifier, x, y, cv=kf)

cross_val_results = cross_val_score(svm_classifier, x, y, cv=kf)

print("Cross-Validation Results (Accuracy):")
for i, result in enumerate(cross_val_results, 1):
    print(f"  Fold {i}: {result * 100:.2f}%")
    
print(f'Mean Accuracy: {cross_val_results.mean()* 100:.2f}%')