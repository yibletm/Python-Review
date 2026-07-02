import pandas as pd
import io
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
from sklearn.impute import SimpleImputer

#Gets the data
data = pd.read_csv("Iris.csv")
#data.info()

#Label encoder turns the species into numerical sets of data
le = LabelEncoder()
temp_data = data
temp_data['Species']=le.fit_transform(temp_data['Species'])
temp_data['Species'].value_counts

#Normalization makes it so the values are shifted and rescaled to be 0 and 1
warnings.filterwarnings("ignore")
normalizer = MinMaxScaler()
temp_data.dropna(axis = 1, inplace = True)
normalized_data = normalizer.fit_transform(temp_data)
pd.DataFrame(normalized_data, columns = temp_data.columns)
temp_data.info()

#Standardization is where the data values are centered around the mean with a certain standard deviation
standard_scaler = StandardScaler
standardized_data = standard_scaler.fit_transform(temp_data)
pd.DataFrame(standardized_data, columns= temp_data.columns)

#OK in the instance of right now being unable to get all of the information on the particular website for any basis of writing
#I will only type in the concepts that are being depicted there to be able to understand what the code is doing.

#Discretization is where contiuous values are made into something more discrete
