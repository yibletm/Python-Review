from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

iris = load_iris() 

X = iris.data 
y = iris.target 
  
feature_names = iris.feature_names 
target_names = iris.target_names 
  
print("Feature names:", feature_names) 
print("Target names:", target_names) 

print("\nType of X is:", type(X)) 

print("\nFirst 5 rows of X:\n", X[:5])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print("X_train Shape:",  X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']
encoder = LabelEncoder()
encoded_feature = encoder.fit_transform(categorical_feature)
print("Encoded feature:", encoded_feature)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred))

sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = log_reg.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)